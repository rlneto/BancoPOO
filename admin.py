from classes import Cliente, Funcionario
from random import randint


def menu(cadastro, funcionarios):
    opt = int(input(f"\nMenu de admin\nSelecione uma das opções do menu.\n1 - Alterar saldo cliente\n"
                    f"2 - Pagar proletário\n3 - Listar clientes\n4 - Listar proletários\n5 - Listar operações do cliente"
                    f"\n6 - Cadastrar cliente\n7 - Cadastrar proletário\n8 - Alterar senha de cliente\n"
                    f"9 - Excluir cliente\n0 - Demitir proletário\nSelecione uma das opções: "))
    if opt == 1:
        cadastro[int(input("Informe o valor da conta a alterar: "))].saldo = \
            (float(input("Informe o novo saldo em R$: ")))
        menu(cadastro, funcionarios)
    elif opt == 2:
        codigo = int(input("Informe o código do proletário: "))
        funcionarios[codigo].saldo += funcionarios[codigo].salario
        print(funcionarios[codigo])
        menu(cadastro, funcionarios)
    elif opt == 3:
        for cliente in cadastro:
            print(cliente)
        menu(cadastro, funcionarios)
    elif opt == 4:
        for funcionario in funcionarios:
            print(funcionario)
        menu(cadastro, funcionarios)
    elif opt == 5:
        cadastro[int(input("Informe o valor da conta: "))].extrato()
        menu(cadastro, funcionarios)
    elif opt == 6:
        cadastro.append(Cliente(str(input("Informe o nome do cliente: ")), int(input("Informe o cpf do cliente: ")),
                        cadastro, 0))
        print("Cliente cadastrado: ", cadastro[-1])
        menu(cadastro, funcionarios)
    elif opt == 7:
        funcionarios.append(Funcionario(str(input("Informe o nome do proletário: ")),
                                        int(input("Informe o cpf do proletário: ")),
                                        str(input("Informe o cargo ocupado: ")), float(input("Informe o salário: ")),
                                            funcionarios))
        print("Proletário cadastrado: ", funcionarios[-1])
        menu(cadastro, funcionarios)
    elif opt == 8:
        codigo = int(input("Informe o número da conta corrente: "))
        cadastro[codigo].senha = int(input("Informe a nova senha: "))
        print("Senha alterada. A nova senha é: ", cadastro[codigo].senha)
        menu(cadastro, funcionarios)
    elif opt == 9:
        cadastro[int(input("Informe o número da conta a ser excluída: "))] = None
        menu(cadastro, funcionarios)
    elif opt == 0:
        funcionarios[int(input("Informe o número da conta a ser excluída: "))] = None
        menu(cadastro, funcionarios)
    else:
        print("Encerrando o programa...")
        exit()


def admin(clientes, funcionarios):
    menu(clientes, funcionarios)


if __name__ == "__main__":
    print("Executando interface de admin...\n")

    with open("nomes.txt", 'r') as arquivo:
        nomes = [nome.strip() for nome in arquivo]

    clientes, funcionarios = [], []

    for iteracao in range(50):
        clientes.append(Cliente(nomes[randint(0, len(nomes)) - 1], randint(100000000000, 999999999999), clientes,
                                randint(1000, 9999)))
        funcionarios.append(Funcionario(nomes[randint(0, len(nomes)) - 1], randint(100000000000, 999999999999), "cargo",
                                        randint(1000, 9999), funcionarios))

    admin(clientes, funcionarios)
