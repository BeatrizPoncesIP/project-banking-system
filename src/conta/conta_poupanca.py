from conta.conta_deposito import Conta_Deposito


class Conta_Poupanca(Conta_Deposito):

    '''

    A conta poupança é um tipo de conta de depósito
    que na verdade é uma aplicação financeira.
    Ao depositar dinheiro nessa conta (caderneta de poupança),
    o valor passa a render juros mensais.

    Desde 2012, o rendimento da poupança se baseia na
    taxa de juros básica da economia brasileira,
    a Selic, seguindo as regras abaixo:

    ●  Se a taxa Selic estiver acima de 8,5% ao ano,
    a poupança rende 0,5% sobre o valor depositado + Taxa Referencial (TR).
    ●  Se a taxa Selic estiver igual ou abaixo de 8,5% ao ano,
    a poupança rende 70% da Selic + TR.
    ●  A conta poupança só permite as funções de saque, depósito e transferência.

    '''

    pass