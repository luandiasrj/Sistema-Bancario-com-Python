menu = """
Escolha uma das opções abaixo:
--------------------------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
--------------------------------
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            continue

        saldo += valor
        extrato += f" Depósito" + f"R$ {valor:.2f}".rjust(30, " ") + "\n"

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("Operação falhou! O valor informado é invalido.")
            continue
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            continue
        if valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
            continue
        if numero_saques == LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            continue

        saldo -= valor
        extrato += f" Saque" + f"R$ {valor:.2f}".rjust(33, " ") + "\n"
        numero_saques += 1

    elif opcao == "e":
        print(" EXTRATO ".center(40, '='))
        print("\n   Não foram realizadas movimentações.\n" if extrato == "" else extrato)
        print(f"Saldo: R$ {saldo:.2f}".rjust(39, " "))
        print("=" * 40)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
