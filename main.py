import textwrap


def menu():
    menu = """
    Escolha uma das opções abaixo:
    ============= Menu =============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNovo Usuário
    [c]\tNova Conta
    [l]\tListar Contas
    [q]\tSair
    --------------------------------
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("\nOperação falhou! O valor informado é inválido.")
    else:
        saldo += valor
        extrato += f" Depósito" + f"R$ {valor:.2f}".rjust(30, " ") + "\n"
        print("\nDepósito efetuado com sucesso!")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("\nOperação falhou! O valor informado é invalido.")

    elif valor > saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif valor > limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif numero_saques == limite_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    else:
        saldo -= valor
        extrato += f" Saque" + f"R$ {valor:.2f}".rjust(33, " ") + "\n"
        numero_saques += 1
        print("\nSaque efetuado com sucesso!")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\nExtrato".center(40, '='))
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}".rjust(39, " "))
    print("=" * 40)


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
    endereco = input(
        "Informe o endereço (logradouro, número - bairro - cidade / estado): ")

    usuarios.append({"nome": nome, "cpf": cpf,
                    "data_nascimento": data_nascimento, "endereco": endereco})
    print(f"\nUsuário {nome} cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario is None:
        print("\nUsuário não encontrado.")
        return None
    else:
        print(f"\nConta para o {usuario['nome']} cadastrada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        Conta:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 40)
        print(textwrap.dedent(linha))

    if len(contas) == 0:
        print("\nNenhuma conta cadastrada.")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 0

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "n":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta += 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()
