# Backlog do Produto


|Data|Versão|Descrição|Autor|
|:--:|:--:|:--:|:---:|
| 07/03/2021 | 0.1 | Versão inicial do backlog | João Vitor Alves |
| 09/03/2021 | 0.2 | Separação do épico Usuários | Kevin |
| 09/03/2021 | 0.3 | Adicionando Tema estratégico | Kevin |
| 18/03/2021 | 0.4 | Correções na estrutura do backlog | Nilo Mendonça |
| 23/03/2021 | 0.5 | Adição dos critérios de aceitação as histórias de Usuários | Nilo Mendonça |


## 1. Tema Estratégico
|Tema|Descrição|
|:--:|:--:|
|TE01| Sistema para disponibilização de monitorias da UnB|


## 2. Épicos

|Épicos|Descrição|
|:--:|:--:|
|EP01|Gerenciamento de Usuários|
|EP02|Gerenciamento de monitorias|


## 3. Features

|Feature|Épico|Descrição|
|:--:|:--:|:--:|
|FE01|EP01|  Gerenciamento de cadastro na aplicação |
|FE2|EP01| Gerenciamento de login na aplicação |
|FE3|EP02| Cadastros em monitorias |
|FE4|EP02|  Informações de monitorias |
|FE5|EP02| Requisições com monitorias |


## 4. Histórias de Usuários
*O termo "Usuário" se refere a ambos os tipos de personas, tanto professores quanto alunos

|Feature|ID|Descrição|Critérios de aceitação|
|:--:|-----|:--:|-----|
|FE01|US01| Eu, como Professor desejo me cadastrar na aplicação| - Criação da página de cadastro para novos professores<br>- Envio das informações ao banco de dados |
|FE01|US02|  Eu, como Professor desejo validar meu email cadastrado| - Criação da requisição para validação de email<br>- Criação do botão para chamada da requisição |
|FE02|US03|  Eu, como Professor desejo efetuar login na aplicação| - Criação da página de login<br>- Envio das informações ao banco de dados |
|FE02|US04|  Eu, como Professor desejo poder recuperar minha senha| - Criação da página de recuperação de senha<br>- Envio do email de recuperação de senha para o Professor |
|FE03|US05|  Eu, como professor desejo cadastrar monitorias| - Criação da página de cadastro para novas monitorias<br>- Envio das informações ao banco de dados |
|FE03|US06| Eu, como aluno desejo me cadastrar em monitorias|  - Criação da página para cadastro em monitorias<br>- Envio das informações ao email disponibilizado pelo Professor|
|FE04|US07| Eu, como Usuário desejo visualizar as monitorias cadastradas| - Criação da página para visualização de monitorias |
|FE04|US08| Eu, como Usuário desejo buscar monitorias utilizando filtros de busca| - Criação da página de busca por monitorias<br>- Criação do formulário para os filtros de busca<br>- Disponibilização das monitorias de acordo com a pesquisa e os filtros |
|FE04|US09| Eu, como aluno desejo ter informações referentes ao IRA necessário para me cadastrar em uma monitoria| - Disponibilização das informações na página da monitoria |
|FE04|US10|  Eu, como Usuário desejo ver a quantidade de alunos cadastrados em uma vaga de monitoria|  - Disponibilização das informações na página da monitoria |
|FE05|US11| Eu, como professor desejo receber um email com as informações de cadastro do aluno em monitoria| - Envio das informações ao email disponibilizado pelo Professor |
|FE05|US12|  Eu, como Usuário desejo compartilhar vagas de monitoria em redes sociais| - Criação do método de compartilhamento das informações da monitoria no Facebook<br> - Criação do método de compartilhamento das informações da monitoria no WhatsApp |
|FE05|US13|  Eu, como Usuário desejo salvar vagas de monitoria do meu interesse| - Criação de um menu lateral para armazenamento das monitorias salvas<br>- Criação dos métodos para adição e remoção das monitorias da lista de monitorias salvas |

## 5. Requisitos não funcionais

|ID|Descrição|
|:--:|:--:|
| RNF01 | A aplicação deve fazer a verificação do e-mail cadastrado pelo Usuário |
| RNF02 | A aplicação deve ser implementada para a plataforma web |