menu = """
[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato

=> """

saldo = 0
limite_saque = 500
extrato = ""
tamanho_extrato = 50
tamanho_coluna1_extrato = 20
tamanho_coluna2_extrato = tamanho_extrato - tamanho_coluna1_extrato - 3
saques_hoje = 0
SAQUES_DIARIOS_MAX = 3

while True:

    opcao = int(input(menu))
    print()

    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))
        print()

        if valor > 0:
            saldo += valor
            extrato += "Depósito:".ljust(tamanho_coluna1_extrato) + "R$ " + f"{valor:.2f}".rjust(tamanho_coluna2_extrato) + "\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        print()

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite_saque:
            print("Operação falhou! O valor do saque excede o limite.")

        elif saques_hoje >= SAQUES_DIARIOS_MAX:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor <= 0:
            print("Operação falhou! O valor informado é inválido.")

        else:
            saldo -= valor
            extrato += "Saque:".ljust(tamanho_coluna1_extrato) + "R$ " + f"{valor:.2f}".rjust(tamanho_coluna2_extrato) + "\n"
            saques_hoje += 1
            print("Saque realizado com sucesso!")

    elif opcao == 3:

        print("  EXTRATO  ".center(tamanho_extrato, "=") + "\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\n" + "Saldo:".ljust(tamanho_coluna1_extrato) + "R$ " + f"{saldo:.2f}".rjust(tamanho_coluna2_extrato) + "\n")
        print("".center(tamanho_extrato, "="))

    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")