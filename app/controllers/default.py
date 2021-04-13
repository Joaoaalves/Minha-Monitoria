from app import app
import ast
import flask
import pyrebase
import datetime
from flask_mail import Mail, Message
import re
import heapq

try:
	with open("config/firebase.key", 'r') as f:
		app.secret_key = f.readline()
except:
	print("Arquivo firebase.key não encontrado!")
	exit()

try:
	with open("config/firebase.cfg", 'r') as f:
		firebaseConfig = ast.literal_eval(f.read())
except:
	print("Arquivo firebase.cfg não encontrado!")	
	exit()

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()
usuario = ""

with open("config/mail.key", 'r') as f:
	mail_username = f.readline()
	mail_username = mail_username[:-1]
	mail_password = f.readline()

app.config.update({
	'MAIL_SERVER' : 'smtp.gmail.com',
	'MAIL_PORT' : 465,
	'MAIL_USERNAME' : mail_username,
	'MAIL_PASSWORD' : mail_password,
	'MAIL_USE_TLS' : False,
	'MAIL_USE_SSL' : True
})
mail = Mail(app)

@app.route("/", methods=['GET', 'POST'])
def home():
	try:
		emailVerificado = auth.get_account_info(flask.session['usuario'])['users'][0]['emailVerified']
		email = auth.get_account_info(flask.session['usuario'])['users'][0]['email']
		nome =  db.child("professores").child(retornarChave(email)).child('nome').get().val()
	except:
		emailVerificado = False
		email = None
		nome = None
	monitorias = db.child("monitorias").get()

	monitoriasSalvas = []
	for i in range(0,15):
		try:
			if flask.session['chave'+str(i)] != '':
				monitoriasSalvas.append(flask.session['chave'+str(i)])
		except:
			flask.session['chave'+str(i)] = ''

	if flask.request.method == 'POST':
		pesquisa = flask.request.form['busca']
		campus = flask.request.form['campus']
		return flask.redirect('/busca?pesquisa='+pesquisa+'&campus='+campus)
	return flask.render_template('home.html', dados=[email, monitorias.val(), emailVerificado, nome, monitoriasSalvas])

@app.route("/login", methods=['GET', 'POST'])
def login():
	if flask.request.method == 'POST':
		tipo = flask.request.form['tipo']
		if tipo == 'login':
			email = flask.request.form['email']
			senha = flask.request.form['senha']

			try:
				usuario = auth.sign_in_with_email_and_password(email, senha)
				flask.session['usuario'] = usuario['idToken']
				return flask.redirect('/')
			except:
				return flask.render_template('login.html', dados=["Erro! Tente novamente", ""])
		elif tipo == 'cadastro':
			nome = flask.request.form['nome']
			email = flask.request.form['email']
			senha = flask.request.form['senha']
			
			try:
				usuario = auth.create_user_with_email_and_password(email, senha)
				flask.session['usuario'] = usuario['idToken']
				db.child("professores").child(retornarChave(email)).child("nome").set(nome)
				return flask.redirect('/')
			except:
				return flask.render_template('login.html', dados=["Erro! Tente novamente", ""])
		
		else:
			email = flask.request.form['email']
			try:
				auth.send_password_reset_email(email)
				return flask.render_template('login.html', dados=["", "true"])
			except:
				return flask.render_template('login.html', dados=["", "false"])
		
	return flask.render_template('login.html', dados=["", ""])

@app.route("/novaMonitoria", methods=['GET', 'POST'])
def novaMonitoria():
	if flask.request.method == 'POST':
		dados = {}
		if flask.request.form['campus'] and flask.request.form['disciplina'] and flask.request.form['horario'] and flask.request.form['codigo'] and flask.request.form['turma'] and flask.request.form['vagas']:
			dados = {
				"nome": "",
				"email": "",
				"campus": flask.request.form['campus'],
				"disciplina": flask.request.form['disciplina'],
				"horario": flask.request.form['horario'],
				"codigo": flask.request.form['codigo'],
				"turma": flask.request.form['turma'],
				"vagas": flask.request.form['vagas'],
			}
		else:
			return flask.render_template('novaMonitoria.html', dados="false")		

		try:
			dados['email'] =  auth.get_account_info(flask.session['usuario'])['users'][0]['email']
			dados['nome'] =  db.child("professores").child(retornarChave(dados['email'])).child('nome').get().val()
			db.child("monitorias").push(dados)
			return flask.redirect('/')
		except:
			return flask.render_template('novaMonitoria.html', dados="false")
	return flask.render_template('novaMonitoria.html')

@app.route("/monitoria", methods=['GET', 'POST'])
def monitoria():
	chave = flask.request.args.get('chave', None)
	monitoria = db.child("monitorias").child(chave).get().val()

	if monitoria:
		codigo = monitoria['codigo']
		disciplina = monitoria['disciplina']
		turma = monitoria['turma']
		vagas = monitoria['vagas']
		email = monitoria['email']

		try:
			monitoria['qtdInscritos'] = len(monitoria['IRAs'])
			if float(vagas) > len(monitoria['IRAs']):
				monitoria['notaIra'] = 0
			else:
				temp = []
				for i in monitoria['IRAs']:
					print(monitoria['IRAs'][i])
					temp.append(float(monitoria['IRAs'][i]))
				notaIra = heapq.nlargest(int(vagas),temp)
				monitoria['notaIra'] = notaIra[-1]
		except:
			monitoria['qtdInscritos'] = 0
			monitoria['notaIra'] = 0

	mensagem = None

	if flask.request.method == 'POST':
		dados = "1. Código SIGAA da disciplina " + codigo
		dados = dados + "\n2. Nome da disciplina no SIGAA: " + disciplina
		dados = dados + "\n3. Turma: " + turma
		dados = dados + "\n4. Vagas da turma: " + vagas
		dados = dados + "\n\n5. Nome do candidato(a): " + flask.request.form['nome']
		dados = dados + "\n6. Matrícula do candidato(a): " + flask.request.form['matricula']
		dados = dados + "\n7. IRA: " + flask.request.form['ira']
		dados = dados + "\n8. Menção do candidato(a): " + flask.request.form['mencao']
		dados = dados + "\n9. E-mail do candidato(a): " + flask.request.form['email']
			
		msg = Message("Monitoria UnB",
			sender = 'minhamonitoria@yahoo.com',
			recipients = [email],
			body= dados
		)

		db.child("monitorias").child(chave).child("IRAs").push(flask.request.form['ira'])

		try:
			mail.send(msg)
			mensagem = "Mensagem enviada com sucesso!"
			return flask.render_template('monitoria.html', dados=[monitoria, chave, mensagem])
		except:
			mensagem = "Erro! Tente novamente"
			return flask.render_template('monitoria.html', dados=[monitoria, chave, mensagem])

	return flask.render_template('monitoria.html', dados=[monitoria, chave, mensagem])

@app.route('/busca', methods=['GET', 'POST'])
def busca():
	pesquisa = flask.request.args.get('pesquisa', None)
	campus = flask.request.args.get('campus', None)

	try:
		emailVerificado = auth.get_account_info(flask.session['usuario'])['users'][0]['emailVerified']
		email = auth.get_account_info(flask.session['usuario'])['users'][0]['email']
		nome =  db.child("professores").child(retornarChave(email)).child('nome').get().val()
	except:
		emailVerificado = False
		email = None
		nome = None
	monitorias = db.child("monitorias").get()
	monitoriasFiltrada = []
	for i in monitorias.val():
		if (campus == 'todos' or monitorias.val()[i]['campus'] == campus) and (re.search(pesquisa.lower(), monitorias.val()[i]['nome'].lower()) or re.search(pesquisa.lower(), monitorias.val()[i]['disciplina'].lower()) or re.search(pesquisa.lower(), monitorias.val()[i]['codigo'].lower())):
			temp = monitorias.val()[i]
			temp['chave'] = i
			monitoriasFiltrada.append(temp)

	if flask.request.method == 'POST':
		pesquisa = flask.request.form['busca']
		campus = flask.request.form['campus']
		return flask.redirect('/busca?pesquisa='+pesquisa+'&campus='+campus)

	monitoriasSalvas = []
	for i in range(0,15):
		try:
			if flask.session['chave'+str(i)] != '':
				monitoriasSalvas.append(flask.session['chave'+str(i)])
		except:
			flask.session['chave'+str(i)] = ''

	return flask.render_template('busca.html', dados=[email, monitoriasFiltrada, emailVerificado, nome, monitoriasSalvas, pesquisa, monitorias.val()])

@app.route('/logout')
def logout():
	auth.current_user = None
	flask.session.clear()
	return flask.redirect('/')
	return flask.render_template('login.html')

@app.route('/ativarConta')
def ativarConta():
	try:
		auth.send_email_verification(flask.session['usuario'])
		return "Enviado com sucesso!"
	except:
		return "Erro"

@app.route('/salvar')
def salvar():
	chave = flask.request.args.get('chave', None)
	for i in range(0,15):
		if flask.session['chave'+str(i)] == '':
			flask.session['chave'+str(i)] = chave
			break
	return chave

@app.route('/removerMonitoriaSalva')
def remover():
	chave = flask.request.args.get('chave', None)
	for i in range(0,15):
		if flask.session['chave'+str(i)] == chave:
			flask.session['chave'+str(i)] = ''
	return chave

@app.route('/excluir')
def excluir():
	chave = flask.request.args.get('chave', None)
	print(chave)
	try:
		db.child("monitorias").child(chave).remove()
		return flask.redirect('/')
	except:
		return flask.redirect('/')

def retornarChave(email):
	chave = ""
	for i in email:
		if i == "@":
			break
		chave = chave + i
	return chave