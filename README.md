# Otimizando o Sistema Bancário com Funções Python
Este repositório contém a entrega de desafio:  __Otimizando com funções Python__ desenvolvido durante o bootcamp: __Potência Tech powered by iFood | Ciências de Dados com Python__.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

* __Depositar:__ permite ao usuário adicionar um valor ao saldo da conta;
* __Sacar:__ permite ao usuário retirar um valor do saldo da conta (não pode exceder o saldo atual nem um limite estabelecido);
* __Extrato:__ exibe todas as movimentações realizadas na conta, bem como o saldo atual;
* __Novo Usuário:__ permite a crição de um novo usuário;
* __Nova Conta:__ cria uma nova conta para um usuário que já existe;
* __Listar Contas:__ exibe todas as contas existentes e seus usuários;
* __Sair:__ encerra a execução do sistema.

## Uso
O usuário é recebido com um menu de opções. Para cada operação, o usuário deve digitar a letra correspondente à ação que deseja realizar.

## Demonstração

<p align="center">
  <img src="Marcos J. Penteado.png" alt="Demonstração do Sistema Bancário"/>
</p>

## Limitações

O sistema está limitado a um saque máximo de R$ 500 e permite um máximo de 3 saques. Se o usuário tentar realizar um saque maior que o saldo atual ou maior que o limite estabelecido, ou tentar realizar mais de 3 saques, a operação será rejeitada e uma mensagem de erro será exibida.

## Contribuições

Seja bem-vindo(a) para realizar um fork ou abrir um `issue` ou `pull request` para sugerir melhorias ou correções. Toda contribuição é bem-vinda!