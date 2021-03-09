from app import app
import flask
import pyrebase
import datetime
from flask_mail import Mail, Message

app.secret_key = 'dfn3e1QScX9o6u0eDGw2yCfh2yBvUR6'

firebaseConfig = {
	"apiKey": "AIzaSyCf2BUR63Xou0eDGwwtDMtRltpwgfneQSc",
	"authDomain": "minha-monitoria.firebaseapp.com",
	"databaseURL": "https://minha-monitoria-default-rtdb.firebaseio.com",
	"projectId": "minha-monitoria",
	"storageBucket": "minha-monitoria.appspot.com",
	"messagingSenderId": "658905609079",
	"appId": "1:658905609079:web:4264d25b50cd861f83e772",
	"measurementId": "G-PY1W0J54VE",
	"serviceAccount": "app/controllers/serviceAccountCredentials.json"
}
firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()
usuario = ""
mail = Mail()

app.config['MAIL_SERVER']='smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'minhamonitoria@yahoo.com'
app.config['MAIL_PASSWORD'] = 'kygjanerwvyeuuhc'	#fga123456
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)

# ENVIAR EMAIL DE VERIFICACAO
# auth.send_email_verification(user["idToken"])

# ENVIAR EMAIL RECUPERACAO CONTA
# auth.send_password_reset_email("fula@f.com")

# PUSH DADOS
# db.child("users").push(dado)

# ATUALIZAR DADOS
# db.child("users").update({"nome": "Fulano"})

# REMOVER DADOS
# db.child("users").child("Ciclano").remove()

# RETORNAR DADOS
# users = db.child("users").get()

@app.route("/")
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
	return flask.render_template('home.html', dados=[email, monitorias.val(), emailVerificado, nome])

@app.route("/login", methods=['GET', 'POST'])
def login():
	if flask.request.method == 'POST':
		email = flask.request.form['email']
		senha = flask.request.form['senha']
		
		try:
			usuario = auth.sign_in_with_email_and_password(email, senha)
			flask.session['usuario'] = usuario['idToken']
			return flask.redirect('/')
		except:
			return flask.render_template('login.html', dados="Erro! Tente novamente")
	return flask.render_template('login.html')

@app.route("/recuperarSenha", methods=['GET', 'POST'])
def recuperarSenha():
	if flask.request.method == 'POST':
		email = flask.request.form['email']
		try:
			auth.send_password_reset_email(email)
			return flask.redirect('/login')
		except:
			return flask.render_template('recuperarSenha.html', dados="Erro! Tente novamente")
	return flask.render_template('recuperarSenha.html')

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
	if flask.request.method == 'POST':
		nome = flask.request.form['nome']
		email = flask.request.form['email']
		senha = flask.request.form['senha']
		
		try:
			usuario = auth.create_user_with_email_and_password(email, senha)
			flask.session['usuario'] = usuario['idToken']
			db.child("professores").child(retornarChave(email)).child("nome").set(nome)
			return flask.redirect('/')
		except:
			return flask.render_template('cadastro.html', dados="Erro! Tente novamente")
	return flask.render_template('cadastro.html')

@app.route("/novaMonitoria", methods=['GET', 'POST'])
def novaMonitoria():
	if flask.request.method == 'POST':
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

		try:
			dados['email'] =  auth.get_account_info(flask.session['usuario'])['users'][0]['email']
			dados['nome'] =  db.child("professores").child(retornarChave(dados['email'])).child('nome').get().val()
			db.child("monitorias").push(dados)
			return flask.redirect('/')
		except:
			return flask.render_template('novaMonitoria.html', dados="Erro! Tente novamente")
	return flask.render_template('novaMonitoria.html')

@app.route("/monitoria")
def monitoria():
	chave = flask.request.args.get('chave', None)
	monitoria = db.child("monitorias").child(chave).get().val()
	return flask.render_template('monitoria.html', dados=monitoria)

@app.route("/mensagem", methods=['GET', 'POST'])
def mensagem():
	codigo = flask.request.args.get('codigo', None)
	disciplina = flask.request.args.get('disciplina', None)
	turma = flask.request.args.get('turma', None)
	vagas = flask.request.args.get('vagas', None)
	email = flask.request.args.get('email', None)

	if flask.request.method == 'POST':
		try:
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

			mail.send(msg)
			return flask.redirect('/')
		except:
			return flask.render_template('mensagem.html', dados="Erro! Tente novamente")
	return flask.render_template('mensagem.html')

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
	# flask.session['chave'] = chave
	print(chave)
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