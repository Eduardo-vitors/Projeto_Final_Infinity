# Documentação do Código do Projeto Final Da Infinity School

### Minha missão era criar uma plataforma que aborde os requisitos :
1. Desenvolver um sistema de controle de acesso que permita apenas usuários autorizados a acessar áreas restritas das instalações das Indústrias Wayne;
1. Implementar uma autenticação e autorização para diferentes tipos de usuários, como funcionários gerentes e administradores de segurança;
1. Crie um painel de controle visualmente atraente que exiba dados relevantes sobre segurança, recursos e atividades dentro das Indústrias Wayne;
1. Desenvolver uma interface para gerenciar recursos internos, como inventário de equipamentos, veículos e dispositivos de segurança;
1. Permitir que os administradores possam adicionar, remover e atualizar informações sobre esses recursos de forma eficiente.

## Informações sobre o Código.

O meu sistema de Controle começa com uma página de Login que vai solicitar nome e senha do usuário que no inicio já está no Banco de Dados para fácil testes. No inicio pode ser utilizados varios Login que estão separados em três áreas .
### LOGIN :
Vou separar os Login nas três profissões para fácil manuseio:
#### Adiministradores
Nome : Bruce - Senha: Batman
Nome : Edu - Senha: Cartoon
#### Gerente
Nome : Du - Senha: Desenho
#### Funcionários
Nome : Clark - Senha: SuperHomem
Nome : Dudu - Senha: Animado

Depois que o Login é confirmado a página de Menu muda pois se for Adiministrador no menu vai aparecer a Logo do Batman e terá acesso a tudo do sistema de controle, mas se por acaso for funcionário ou gerente o menu terá a Logo da empresa Wayne Enterprises.

### Informação sobre o Menu :
 
O menu é dividido em 5 Botões e eu irei explicar a funcionalidade de cada um.

#### Incluir Usuário :

 1.   Só quem pode clicar neste botão é o gerente e o administrador, se for clicado vai aparecer uma área no lado esquerdo onde poderá incluir uma nova pessoa no Banco de Dados e para isso tem que informar o **NOME** , **SENHA** e o **TIPO** e depois disso só clicar no botão **Incluir**, você também vai poder visualizar que tem o botão **Visualiza Lista** que leva para uma nova página aonde vai ter uma tabela que vai mostrar os dados informados de todas as pessoas da Empresa e só quem pode visualizar é o Administrador, o botão **Retornar** volta para o Incluir Usuário.

#### Incluir Recursos :
1. Só quem pode clicar neste botão é o administrador, se for clicado vai aparecer uma área no lado esquerdo onde poderá incluir um novo recurso que para incluir só tem que digitar o **Nome do Objeto** e qual o seu **Tipo** entre o que aparece lá depois só apertar o botão incluir e Pronto.
#### Consultar Recursos :
1. Todos podem Apertar este botão aonde irá mostrar no lado esquerdo ao menu uma tabela com o Nome do Recurso e o seu Tipo
1. Os botões no lado da **TABELA** Remover e Atualizar só pode ser usado pelo Adiministrador.
1. Para fazer o Botão Remover funcionar tem que clicar no Nome do Recurso da tabela até ficar Azul e depois disso ter certeza que é administrador e apertar o botão no mesmo instante o Recurso será removido.
1. Para fazer o Botão Atualizar funcionar tem que ser Administrador clicar no nome do recurso até fica azul e depois clicar no botão Atualizar aonde vai te levar para outra página. Que aparecerá o Campo de **Nome de Recurso** e o **Tipo** para você rescrever e assim em seguida apertar Atualizar para atualização seja feita com sucesso. se olhar bem tem um botão **Retornar** quando apertado irá de voltar para a ***Tabela de Recursos***.
#### Logout :
Se este Botão for Apertado vai sair do Menu e voltar para o Login onde outra pessoa pode entrar com sua *CONTA*. Todos podem Apertar este botão.
#### Encerrar :
Se este Botão for Apertado vai Fechar todo o Sistema. Todos podem Apertar este botão.

