# Minha Monitoria

## Caso de Uso: Fazer cadastro

### 1. Breve descrição
O presente caso de uso descreve a atividade de realização de cadastro no site Minha Monitoria. Basicamente é solicitado ao Professor informações de nome, email e senha, para que sejam armazenadas no banco de dados da aplicação.

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
	
	5. O sistema redireciona o Professor para a tela inicial do site
	
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
- Para FB: são enviadas as informações fornecidas ao banco de dados.

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
    
    2. O sistema apresenta um formulário contendo os seguintes campos a serem preenchidos:
    	- Email
   		- Senha

    3. O Professor informa os dados

    4. O sistema verifica se os campos estão preenchidos (RN01)(RN02)(FE01)

    5. O sistema verifica se as informações disponilizadas pelo professor estão de acordo com as informações existentes no banco de dados (FE02)

    6. O sistema redireciona o Professor para a tela inicial do site

    O caso de uso se encerra.

### 5. Fluxos Alternativos (FA)
Não se aplica.

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

		### 1. Descrição

		### 2. Fluxo Básico de Eventos

		### 3. Fluxos Alternativos

		### Subfluxos

		### Pré-condições

		### Pós-condições

		### Pontos de Extensão

		### Requisitos Especiais

		### Informações Adicionais

## Caso de Uso: Visualizar monitoria

		### 1. Descrição

		### 2. Fluxo Básico de Eventos

		### 3. Fluxos Alternativos

		### Subfluxos

		### Pré-condições

		### Pós-condições

		### Pontos de Extensão

		### Requisitos Especiais

		### Informações Adicionais

## Caso de Uso: Cadastrar-se em uma monitoria

		### 1. Descrição

		### 2. Fluxo Básico de Eventos

		### 3. Fluxos Alternativos

		### Subfluxos

		### Pré-condições

		### Pós-condições

		### Pontos de Extensão

		### Requisitos Especiais

		### Informações Adicionais