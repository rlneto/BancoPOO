from classes import Cliente
from random import randint


def login(cadastro, senha, conta):
    if conta < len(cadastro):
        if cadastro[conta].senha == senha:
            return True
        else:
            return False
    else:
        return False


def menu(cadastro, conta):
    opt = int(input(f"\nMenu da conta {conta}\nSelecione uma das opções do menu.\n1 - Saque\n2 - Transferência\n"
                    f"3 - Deposito\n4 - Emprestimo\n5 - Extrato\n6 - Alterar PIN\n7 - Saldo\n8 - Alternar conta\n"
                    f"9 - Sair\nSelecione uma das opções: "))
    if opt == 1:
        cadastro[conta].saque(float(input("Informe o valor a sacar em R$: ")))
        menu(cadastro, conta)
    elif opt == 2:
        cadastro[conta].transferencia(int(input("Informe a conta de destino: "))
                                      , float(input("Informe o valor a transferir em R$: ")), cadastro)
        menu(cadastro, conta)
    elif opt == 3:
        cadastro[conta].deposito(float(input("Informe o valor em R$ a depositar: ")), conta)
        menu(cadastro, conta)
    elif opt == 4:
        cadastro[conta].emprestimo(float(input("Informe o valor do empréstimo em R$: ")))
        menu(cadastro, conta)
    elif opt == 5:
        cadastro[conta].extrato()
        menu(cadastro, conta)
    elif opt == 6:
        cadastro[conta].senha = int(input("Digite o novo PIN (somente números): "))
        menu(cadastro, conta)
    elif opt == 7:
        print(cadastro[conta])
        menu(cadastro, conta)
    elif opt == 8:
        user(cadastro)
    else:
        print("Encerrando o programa...")
        exit()


def user(clientes):
    print("Login:\n")
    conta = int(input("Informe o número da conta: "))
    senha = int(input("Agora informe o PIN: "))
    if login(clientes, senha, conta):
        menu(clientes, conta)
    else:
        print("Login ou senha inválidos. Tente novamente.")
        print(f"SOMENTE MODO DEV a senha da conta {conta} é: {clientes[conta].senha} .")
        user(clientes)


if __name__ == "__main__":
    print("Executando terminal de usuário...\n")

    with open("nomes.txt", 'r') as arquivo:
        nomes = [nome.strip() for nome in arquivo]

    clientes = []

    for iteracao in range(50):
        clientes.append(Cliente(nomes[randint(0, len(nomes)) - 1], randint(100000000000, 999999999999), clientes,
                                randint(1000, 9999)))
    user(clientes)
