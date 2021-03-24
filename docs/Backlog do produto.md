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
|FE01|US01| Eu, como Professor desejo me cadastrar na aplicação| - O sistema deve enviar as informações ao banco dados<br>- Se o Professor for cadastrado com sucesso na aplicação ele deve ser redirecionado para a página inicial da aplicação<br>- Se ocorrer algum erro durante o cadastro deve ser exibido uma mensagem de erro na página da aplicação |
|FE01|US02|  Eu, como Professor desejo validar meu email cadastrado| - Ao solicitar a validação do email deve ser exibido uma mensagem na página da aplicação informando que o email para validação foi enviado<br>- Caso ocorra algum erro na solicitação deve ser exibido uma mensagem na tela informando o erro<br>- A aplicação deve informar ao Professor se o email está ou não validado<br>- O sistema só deve disponibilizar um meio para solicitar a validação do email caso o email ainda não tenha sido validado |
|FE02|US03|  Eu, como Professor desejo efetuar login na aplicação| - O sistema deve redirecionar o Professor para a página inicial caso o login tenha sido efetuado com sucesso<br>- O sistema deve exibir uma mensagem na tela caso tenha ocorrido algum erro ao efetuar login |
|FE02|US04|  Eu, como Professor desejo poder recuperar minha senha| - O sistema deve redirecionar o Professor para a página de login caso a solicitação de recuperação de senha tenha sido feita com sucesso<br>- O sistema deve exibir uma mensagem na tela caso tenha ocorrido algum erro durante a solicitação |
|FE03|US05|  Eu, como professor desejo cadastrar monitorias| - O sistema só deve permitir o cadastro de novas monitorias por Usuários que tenham validado o email de cadastro<br>- O professor não pode criar monitorias caso tenha campos obrigatórios no formulário em branco<br>- O sistema deve exibir uma mensagem na tela caso tenha ocorrido algum erro ao criar a monitoria<br>- O Professor deve ser redirecionado para a página inicial caso a monitoria tenha sido cadastrada com sucesso |
|FE03|US06| Eu, como Aluno desejo me cadastrar em monitorias| - O Aluno não pode se cadastrar em monitorias caso tenha campos obrigatórios no formulário de cadastro em branco<br>- O sistema deve exibir uma mensagem na tela caso tenha ocorrido algum erro ao fazer a requisição de cadastro em monitoria<br>- O Aluno deve ser redirecionado para a página inicial caso tenha sido cadastrado com sucesso<br>- O sistema deve enviar um email ao Professor com os dados informados pelo Aluno |
|FE04|US07| Eu, como Usuário desejo visualizar as monitorias cadastradas| - O sistema deve exibir as informações preenchidas no cadastro da monitoria pelo Professor |
|FE04|US08| Eu, como Usuário desejo buscar monitorias utilizando filtros de busca| - Caso a busca tenha sido feita deixando o campo de pesquisa em branco, deve-se retornar todas as monitorias cadastradas<br>- Caso não tenha nenhuma monitoria que corresponda a busca deve-se exibir uma lista vazia como resultado da pesquisa |
|FE04|US09| Eu, como aluno desejo ter informações referentes ao IRA necessário para me cadastrar em uma monitoria| - Deve ser exibido a nota necessária do IRA para ser aceito pela vaga baseado nos cadastros anteriores<br>Caso não tenha nenhum cadastro anterior ou a quantidade de cadastros seja inferior a quantidade de vagas deverá ser exibida a nota 0 |
|FE04|US10|  Eu, como Usuário desejo ver a quantidade de alunos cadastrados em uma vaga de monitoria|  - Deve ser exibido a quantidade de cadastros efetuados na monitoria |
|FE05|US11| Eu, como professor desejo receber um email com as informações de cadastro do aluno em monitoria| - O sistema deve enviar um email para Professor quando o Aluno for cadastrado na monitoria |
|FE05|US12|  Eu, como Usuário desejo compartilhar vagas de monitoria em redes sociais| - O sistema deve redirecionar o Usuário para a página da aplicação contendo as informações a serem compartilhadas |
|FE05|US13|  Eu, como Usuário desejo salvar vagas de monitoria do meu interesse| - O sistema deve disponibilizar um menu lateral contendo as monitorias salvas<br>- O sistema deve permitir adicionar e remover monitorias do menu lateral |

## 5. Requisitos não funcionais

|ID|Descrição|
|:--:|:--:|
| RNF01 | A aplicação deve fazer a verificação do e-mail cadastrado pelo Usuário |
| RNF02 | A aplicação deve ser implementada para a plataforma web |