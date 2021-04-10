# Backlog do Produto


|Data|Versão|Descrição|Autor|
|:--:|:--:|:--:|:--:|
| 07/03/2021 | 0.1 | Versão inicial do backlog | João Vitor Alves |
| 09/03/2021 | 0.2 | Separação do épico Usuários | Kevin |
| 09/03/2021 | 0.3 | Adicionando Tema estratégico | Kevin |
| 18/03/2021 | 0.4 | Correções na estrutura do backlog | Nilo Mendonça |
| 23/03/2021 | 0.5 | Adição dos critérios de aceitação as estórias de Usuários | Nilo Mendonça |
| 23/03/2021 | 0.6 | Correções nas estórias de Usuários, na nomeclatura das Features e adição das priorizações | Nilo Mendonça |
| 08/04/2021 | 0.7 | Correções nas estórias de Usuários | Nilo Mendonça |


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

|Feature|Épico|Descrição|Prioridade|
|:--:|:--:|:--:|:--:|
|FE01|EP01| Gerenciar contas na aplicação | alta |
|FE02|EP02| Cadastrar em monitorias | média |
|FE03|EP02| Obter informações de monitorias | média |
|FE04|EP02| Realizar requisições com monitorias | baixa |


## 4. Estórias de Usuários
- *O termo "Usuário" se refere a ambos os tipos de personas, tanto Professores quanto Alunos
- As prioridades das Features possuem uma precedência maior que a prioridade das Estórias de Usuários, ou seja, uma História de Usuário com prioridade alta mas derivado de uma Feature com prioridade média tem prioridade menor que uma História de Usuário com prioridade baixa mas derivada de uma Feature com prioridade alta

|Feature|ID|Descrição|Critérios de aceitação|Prioridade|
|:--:|:--:|:--:|:--:|:--:|
|FE01|US01| Eu, como Professor desejo me cadastrar na aplicação para poder cadastrar monitorias | - Se o Professor for cadastrado com sucesso na aplicação ele deve ser redirecionado para a página inicial da aplicação<br>- Se ocorrer algum erro durante o cadastro deve ser exibido uma mensagem de erro na página da aplicação<br>- Ao se cadastrar na aplicação deve ser enviado um email para a validação do email cadastrado | alta |
|FE01|US02| Eu, como Professor desejo efetuar login na aplicação para poder acessar meus dados na aplicação | - O Professor deve ser redirecionado para a página inicial caso o login tenha sido efetuado com sucesso<br>- Deve ser exibido uma mensagem na tela caso tenha ocorrido algum erro ao efetuar login | alta |
|FE01|US03| Eu, como Professor desejo poder recuperar minha senha para poder acessar a minha conta na aplicação | - Deve ser exibido uma mensagem na tela informando se a solicitação foi ou não realizada com sucesso | média |
|FE02|US04| Eu, como Professor desejo cadastrar monitorias para poder obter monitores para a minha disciplina | - Deve ser permitido o cadastro de novas monitorias apenas por Usuários que tenham validado o email de cadastro<br>- O professor não pode criar monitorias caso algum dos campos Nome, E-mail, Código, Turma, Horário e Vagas estejam em branco no formulário<br>- Deve ser exibido uma mensagem na tela informando se a solicitação foi ou não realizada com sucesso | alta |
|FE02|US05| Eu, como Aluno desejo me cadastrar em monitorias para poder prestar monitoria em uma disciplina | - O Aluno não pode se cadastrar em monitorias caso algum dos campos Nome, E-mail, Matricula, IRA e Menção estejam em branco no formulário de cadastro<br>- Deve ser exibido uma mensagem na tela informando se a solicitação foi ou não realizada com sucesso<br>- Deve ser enviado um email ao Professor com os dados informados pelo Aluno | média |
|FE03|US06| Eu, como Usuário desejo visualizar as monitorias cadastradas para obter as informações referentes a ela | - Deve ser exibido as informações preenchidas no cadastro da monitoria pelo Professor | média |
|FE03|US07| Eu, como Usuário desejo buscar monitorias utilizando filtros de busca para poder encontrar as monitorias do meu interesse | - Caso a busca tenha sido feita deixando o campo de pesquisa em branco, deve-se retornar todas as monitorias cadastradas<br>- Caso não tenha nenhuma monitoria que corresponda a busca deve-se exibir uma lista vazia como resultado da pesquisa | alta |
|FE03|US08| Eu, como Aluno desejo ter informações referentes ao IRA necessário para me cadastrar em uma monitoria | - Deve ser exibido a nota necessária do IRA para ser aceito pela vaga baseado nos cadastros anteriores<br>Caso não tenha nenhum cadastro anterior ou a quantidade de cadastros seja inferior a quantidade de vagas deverá ser exibida a nota 0 | baixa |
|FE03|US09| Eu, como Usuário desejo ver a quantidade de alunos cadastrados em uma vaga de monitoria para saber quais as chances de ser escolhido como monitor | - Deve ser exibido a quantidade de cadastros efetuados na monitoria | baixa |
|FE04|US10| Eu, como Usuário desejo compartilhar vagas de monitoria em redes sociais para poder informar as outras pessoas sobre a sua existência | - O Usuário deve ser redirecionado para a página da rede social contendo as informações a serem compartilhadas | média |
|FE04|US11|  Eu, como Usuário desejo salvar vagas de monitoria do meu interesse para poder acessá-las em outro momento | - Deve ser disponibilizado ao Usuário um menu lateral contendo uma lista de monitorias<br>- Deve ser possível adicionar e remover monitorias da lista | média |

## 5. Requisitos não funcionais

|ID|Descrição|
|:--:|:--:|
| RNF01 | A aplicação deve ser implementada para a plataforma web |
| RNF02 | A aplicação deve ser implementada em Linguagem Python > 3.6 |