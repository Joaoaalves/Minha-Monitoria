# Minha Monitoria

	## Caso de Uso: Fazer cadastro

		### 1. Descrição
			Permitir que o Professor realize o cadastro no site com email.

		### 2. Fluxo Básico de Eventos
			1. O Professor decide realizar o cadastro no site
    
    		2. O sistema apresenta um formulário contendo os seguintes campos a serem preenchidos:
    			- Nome
    			- Email
    			- Senha

    		3. O Professor informa os dados

		    4. O sistema verifica se os campos estão preenchidos

		    5. O sistema realiza o envio das informações ao banco de dados

    		6. O sistema redireciona o Professor para a tela inicial do site

    	O caso de uso se encerra.

		### 3. Fluxos Alternativos

			#### 3.1 Fluxo Alternativo A
				
				1. No passo 4 do fluxo básico, o sistema verifica alguma inconsistência nas informações disponibilizadas pelo Professor

				2. O sistema informa uma mensagem de erro ao Professor

				3. O fluxo retorna ao passo 3 do fluxo básico

		### 4. Informações Adicionais

			#### 4.1 Dados do Professor
				
				##### Campos editáveis
					- Nome
					- Email
						- Deve conter o caracter "@"
						- Deve conter o conjunto de caracteres ".com"
					- Senha
						- Deve conter pelo menos quatro caracteres

	## Caso de Uso: Fazer login

		### 1. Descrição
			Permitir que o Professor realize o acesso ao seu cadastro.

		### 2. Fluxo Básico de Eventos
			1. O Professor decide realizar o login no site
    
    		2. O sistema apresenta um formulário contendo os seguintes campos a serem preenchidos:
    			- Email
    			- Senha

    		3. O Professor informa os dados

    		4. O sistema verifica se os campos estão preenchidos

    		5. O sistema verifica se as informações disponilizadas pelo professor estão de acordo com as informações existentes no banco de dados

    		6. O sistema redireciona o Professor para a tela inicial do site

    	O caso de uso se encerra.

		### 3. Fluxos Alternativos
	
			#### 3.1 Fluxo Alternativo A
				1. No passo 4 do fluxo básico, o sistema verifica alguma inconsistência nas informações disponibilizadas pelo Professor

				2. O sistema informa uma mensagem de erro ao Professor

				3. O fluxo retorna ao passo 3 do fluxo básico

			#### 3.2 Fluxo Alternativo B
				1. No passo 5 do fluxo básico, o sistema verifica não consegue encontrar no banco de dados as informações disponibilizadas pelo Professor

				2. O sistema informa uma mensagem de erro ao Professor

				3. O fluxo retorna ao passo 3 do fluxo básico

		### Informações Adicionais
			
			#### Dados de login
		
				##### Campos editáveis
					- Nome
					- Email
						- Deve conter o caracter "@"
						- Deve conter o conjunto de caracteres ".com"
					- Senha
						- Deve conter pelo menos quatro caracteres

## Caso de Uso: Recuperar senha

		### 1. Descrição

		### 2. Fluxo Básico de Eventos

		### 3. Fluxos Alternativos

		### Subfluxos

		### Pré-condições

		### Pós-condições

		### Pontos de Extensão

		### Requisitos Especiais

		### Informações Adicionais

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