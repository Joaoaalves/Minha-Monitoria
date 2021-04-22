# Especificação de Casos de Uso

## Atores

|Nome|Descrição|
|:--:|:--:|
| Professor | Uma pessoa que pode visualizar, buscar e cadastrar nova monitorias |
| Aluno | Uma pessoa que pode visualizar, buscar e se cadastrar em monitorias existentes |

## Casos de uso

|Nome|Descrição|Atores|Prioridade|
|:--:|:--:|:--:|:--:|
| Fazer cadastro | Permitir que o usuário realize o cadastro no site com seu email | Professor | alta |
| Fazer login | Permitir que o usuário acesse o seu cadastro | Professor | alta |
| Recuperar senha | Permitir que o usuário recupere o acesso ao seu cadastro | Professor | alta |
| Cadastrar nova monitoria | Permitir que o usuário cadastre novas monitorias  | Professor | alta |
| Visualizar monitoria | Permitir que o usuário visualize as vagas de monitoria cadastradas | Aluno, Professor | alta |
| Compartilhar monitoria | Permitir que o usuário compartilhe em redes sociais as vagas de monitorias cadastradas | Aluno, Professor | baixa |
| Buscar monitoria | Permitir que o usuário busque por vagas de monitorias cadastradas no site | Aluno, Professor | média |
| Verificar email | Verificar se o email possui um formato válido e se já se encontra no banco de dados | Professor | alta |
| Verificar senha | Verificar se a senha está de acordo com o email do perfil cadastrado | Professor | alta |
| Exibir mensagem de erro | Exibir mensagem de erro caso o usuário seja impossibilitado de executar alguma ação requerida | Aluno, Professor | baixa |
| Salvar monitoria de interesse | Permitir ao usuário salvar vagas de monitoria em um menu lateral | Aluno, Professor | baixa |
| Cadastrar-se em monitoria | Permitir ao usuário se cadastrar em uma monitoria cadastrada no site | Aluno | alta |

## Diagrama de Casos de Uso

<img src="imgs/Casos_de_uso.png">
