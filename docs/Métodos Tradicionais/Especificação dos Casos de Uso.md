# Minha Monitoria

## Caso de Uso: Fazer cadastro

### 1. Breve descrição
O presente caso de uso descreve a atividade de realização de cadastro de novo usuário no site Minha Monitoria. Basicamente é solicitado ao Professor informações de nome, email e senha, para que sejam armazenadas no banco de dados da aplicação.

### 2. Atores
#### 2.1 Professor
Professor da Universidade de Brasilia que busca monitores para a sua disciplina.

### 3. Condições prévias
Não se aplica.

### 4. Fluxo Básico (FB)
	1. O Professor decide realizar o cadastro no site
    
    2. O sistema apresenta um formulário contendo os seguintes campos a serem preenchidos:
    	- Nome
   		- Email
    	- Senha
	
	3. O Professor informa os dados
	
	4. O sistema verifica se os campos estão preenchidos (RN01)(RN02)(RN03)(FE01)

	5. O sistema realiza o envio das informações ao banco de dados
	
	6. O sistema redireciona o Professor para a tela inicial do site
	
	O caso de uso se encerra.

### 5. Fluxos Alternativos (FA)
Não se aplica.

### 6. Fluxo de Exceção (FE)
#### 6.1 FE01 - Informações incorretas
	1. No passo 4 do FB, o sistema verifica alguma inconsistência nas informações disponibilizadas pelo Professor

	2. O sistema informa uma mensagem de erro ao Professor (RN04)

	3. O fluxo retorna ao passo 3 do FB

### 7. Regras de Negócio (RN)
#### 7.1 RN01 - Validação do Nome
Para que seja considerado válido o nome deve conter ao menos um caracter.

#### 7.2 RN02 - Validação do Email
Para que seja considerado válido o email deve conter:<br>
"@" e ".com" e/ou ".br"

#### 7.3 RN03 - Validação da Senha
Para que seja considerada válida a senha deve conter pelo menos quatro caracteres.

#### 7.4 RN04 - Mensagem de Erro
O sistema deve exibir a mensagem "Erro! Tente novamente".

### 8. Pós-condições
- Para FB: é enviado um email para validação do email cadastrado pelo Professor (verificar se o Professor possuí acesso ao email cadastrado)

### 9. Pontos de extensão
Não se aplica.

## Caso de Uso: Fazer login

### 1. Breve descrição
O presente caso de uso descreve a atividade de realização de login no site Minha Monitoria. Basicamente é solicitado ao Professor informações de email e senha, para que sejam verificados com os dados presentes no banco de dados da aplicação.

### 2. Atores
#### 2.1 Professor
Professor da Universidade de Brasilia que busca monitores para a sua disciplina.

### 3. Condições prévias
- O Professor deve possuir cadastro no site.

### 4. Fluxo Básico (FB)
	1. O Professor decide realizar o login no site
    
    2. O sistema apresenta a opção de recuperação de senha e um formulário contendo os seguintes campos a serem preenchidos:
    	- Email
   		- Senha

    3. O Professor informa os dados

    4. O sistema verifica se os campos estão preenchidos (RN01)(RN02)(FE01)

    5. O sistema verifica se as informações disponilizadas pelo professor estão de acordo com as informações existentes no banco de dados (FE02)

    6. O sistema realiza o login

    6. O sistema redireciona o Professor para a tela inicial do site

    O caso de uso se encerra.

### 5. Fluxos Alternativos (FA)
#### 5.1 FA01 - Recuperar senha
	1. No passo 2 do FB o Professor selecione o opção Recuperar senha

	2. O sistema apresenta um formulário contendo o seguinte campo a ser preenchido:
    	- Email

    3. O Professor informa os dados

    4. O sistema verifica se o campo está preenchido (RN01)(FE01)

    5. O sistema verifica se as informações disponilizadas pelo professor estão de acordo com as informações existentes no banco de dados (FE02)
    
    4. O sistema envia uma mensagem no email informado para alteração de senha

    3. O fluxo retorna ao passo 2 do FB

### 6. Fluxo de Exceção (FE)
#### 6.1 FE01 - Informações incorretas
	1. No passo 4 do FB, o sistema verifica alguma inconsistência nas informações disponibilizadas pelo Professor

	2. O sistema informa uma mensagem de erro ao Professor (RN03)

	3. O fluxo retorna ao passo 3 do FB

#### 6.2 FE02 - Dados não encontrados
	1. No passo 5 do FB, o sistema não consegue encontrar no banco de dados as informações disponibilizadas pelo Professor

	2. O sistema informa uma mensagem de erro ao Professor (RN03)

	3. O fluxo retorna ao passo 3 do FB

### 7. Regras de Negócio (RN)
#### 7.1 RN01 - Validação do Email
Para que seja considerado válido o email deve conter:<br>
"@" e ".com" e/ou ".br"

#### 7.2 RN02 - Validação da Senha
Para que seja considerada válida a senha deve conter pelo menos quatro caracteres.

#### 7.3 RN03 - Mensagem de Erro
O sistema deve exibir a mensagem "Erro! Tente novamente".

### 8. Pós-condições
Não se aplica.

### 9. Pontos de extensão
Não se aplica.

## Caso de Uso: Cadastrar nova monitoria

### 1. Breve descrição
O presente caso de uso descreve a atividade de realização de cadastro de uma nova monitoria no site Minha Monitoria. Basicamente é solicitado ao Professor algumas informações referentes a disciplina para que sejam armazenadas no banco de dados da aplicação.

### 2. Atores
#### 2.1 Professor
Professor da Universidade de Brasilia que busca monitores para a sua disciplina.

### 3. Condições prévias
- O Professor precisa ter executado o caso de uso Fazer login
- O email cadastrado pelo Professor precisa ter sido validado

### 4. Fluxo Básico (FB)
	1. O Professor decide realizar o cadastro de uma nova monitoria no site
    
    2. O sistema apresenta um formulário contendo os seguintes campos a serem preenchidos:
    	- Disciplina
   		- Campus
    	- Código
    	- Turma
    	- Horário
    	- Vagas
	
	3. O Professor informa os dados
	
	4. O sistema verifica se os campos estão preenchidos (RN01)(RN02)(RN03)(RN04)(RN05)(RN06)(FE01)

	5. O sistema envia as informações ao banco de dados

	6. O sistema redireciona o Professor para a tela inicial do site
	
	O caso de uso se encerra.

### 5. Fluxos Alternativos (FA)
Não se aplica.

### 6. Fluxo de Exceção (FE)
#### 6.1 FE01 - Informações incompletas
	1. No passo 4 do FB, o sistema verifica alguma inconsistência nas informações disponibilizadas pelo Professor

	2. O sistema informa uma mensagem de erro ao Professor (RN07)

	3. O fluxo retorna ao passo 3 do FB

### 7. Regras de Negócio (RN)
#### 7.1 RN01 - Validação da Disciplina
Para que seja considerado válido o nome da disciplina deve conter ao menos um caracter.

#### 7.2 RN02 - Validação do Campus
Para que seja considerado válido o Professor deve selecionar entre os campus:
- Darcy Ribeiro
- FGA
- FCE
- FUP

#### 7.3 RN03 - Validação do Código
Para que seja considerado válido o código da disciplina deve conter ao menos um caracter.

#### 7.4 RN04 - Validação da Turma
Para que seja considerado válido a turma da disciplina deve conter ao menos um caracter.

#### 7.5 RN05 - Validação do Horário
Para que seja considerado válido o horário da disciplina deve conter ao menos um caracter.

#### 7.6 RN06 - Validação das Vagas
Para que seja considerado válido a quantidade de vagas da disciplina deve conter um número acima de 0.

#### 7.7 RN07 - Mensagem de erro
O sistema deve exibir a mensagem "Erro! Tente novamente".

### 8. Pós-condições
Não se aplica.

### 9. Pontos de extensão
Não se aplica.

## Caso de Uso: Visualizar monitoria

### 1. Breve descrição
O presente caso de uso descreve a atividade de visualização das informações cadastradas em uma monitoria no site Minha Monitoria. Basicamente é disponibilizado ao Usuário o acesso a todas as monitorias cadastradas, assim como um meio de efetuar buscas utlizando informações como o nome da disciplina, o código da disciplina ou o ńome do professor da disciplina.

### 2. Atores
#### 2.1 Usuário
Se refere a alunos e professores da Universidade de Brasília que desejam obter informações a respeito de vagas de monitorias.

### 3. Condições prévias
Não se aplica.

### 4. Fluxo Básico (FB)
	1. O Usuário decide visualizar informações referentes a uma determinada monitoria
    
    2. O sistema apresenta uma lista contendo as monitorias cadastradas no site e um campo de pesquisa contendo os campos:
    	- Nome (RN01)
    	- Campus (RN02)
	
	3. O Usuário acessa as informações da monitoria contendo os dados:
		- Disciplina
   		- Campus
		- Nome
		- Email
		- Código
		- Turma
		- Horário
		- Vagas
		- Quantidade de inscritos (RN03)
		- Nota IRA (RN04)
	
	O caso de uso se encerra.

### 5. Fluxos Alternativos (FA)
#### 5.1 FA01 - Busca por monitoria
	1. No passo 2 do FB, o Usuário preenche as informações do campo de pesquisa contendo os campos:
		- Nome (RN01)
		- Campus (RN02)
	e efetua a busca

	2. O sistema exibe uma lista filtrada de acordo com os campos de pesquisa (RN05)

	3. O fluxo retorna ao passo 3 do FB

#### 5.2 FA02 - Cadastrar-se em uma monitoria ????????????????????

### 6. Fluxo de Exceção (FE)
Não se aplica.

### 7. Regras de Negócio (RN)
#### 7.1 RN01 - Nome de pesquisa
- O nome inserido na pesquisa pode se referir ao nome da disciplina, ao código da disciplina ou ao nome do professor que ministra a disciplina.
- Caso o nome seja deixado em branco o resultado da pesquisa deve incluir todos os nomes cadastrados nas monitorias do banco de dados

#### 7.2 RN02 - Campus da pesquisa
Para que seja considerado válido o Usuário deve selecionar entre os campus:
- Todos
- Darcy Ribeiro
- FGA
- FCE
- FUP

#### 7.3 RN03 - Quantidade de inscritos
A cada inscrição realizada o sistema deve incrementar em uma unidade o número de inscritos.

#### 7.4 RN04 - Nota IRA
- Ordenando os inscritos na monitoria em ordem decrescente da nota IRA, o sistema deve exibir a nota do cadastro que ocupa a posição de quantidade de vagas disponíveis
- Caso não tenha nenhum cadastro anterior ou a quantidade de cadastros seja inferior a quantidade de vagas deverá ser exibida a nota 0

#### 7.5 RN05 - Filtragem de busca
- O sistema deve exibir qualquer cadastro que possua o mesmo conjunto de caracteres inseridos no capo de pesquisa no nome da disciplina e/ou no código da disciplina e/ou no nome do professor que ministra a disciplina
- Caso o campus selecionado seja o "Todos", o sistema não deve realizar filtragem por campus
- Caso o campus selecionado seja diferente de "Todos", o sistema deve exibir apenas as monitorias em que as disciplinas sejam ministradas no campus selecionado pelo Usuário

### 8. Pós-condições
Não se aplica.

### 9. Pontos de extensão
Não se aplica.

## Caso de Uso: Cadastrar-se em uma monitoria ???????????????