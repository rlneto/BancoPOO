from classes import Funcionario
from random import randint


def menu(cadastro, conta):
    opt = int(input(f"\nMenu da conta {conta}\nSelecione uma das opções do menu.\n1 - Saque\n2 - Saldo\n"
                    f"3 - Pedir demissão\n4 - Sair\n"
                    f"nSelecione uma das opções: "))
    if opt == 1:
        cadastro[conta].saque(float(input("Informe o valor a sacar em R$: ")))
        menu(cadastro, conta)
    elif opt == 2:
        print(cadastro[conta])
        menu(cadastro, conta)
    elif opt == 3:
        cadastro[conta] = None
        print("Você foi demitido.\n")
        proletario(cadastro)
    else:
        print("Encerrando o programa...")
        exit()


def proletario(funcionarios):
    print("Login:\n")
    conta = int(input("Bem-vinde ao banco que te remunera muitíssimo bem!\nInforme seu código de funcionário: "))
    if conta >= len(funcionarios):
        print("Código inválido. Tente novamente.")
        proletario(funcionarios)
    else:
        menu(funcionarios, conta)


if __name__ == "__main__":
    print("Executando terminal de funcionário...\n")

    with open("nomes.txt", 'r', encoding='utf-8') as arquivo:
        nomes = [nome.strip() for nome in arquivo]

    funcionarios = []

    for iteracao in range(50):
        funcionarios.append(Funcionario(nomes[randint(0, len(nomes)) - 1], randint(100000000000, 999999999999), "cargo",
                                        randint(1000, 9999), funcionarios))

    proletario(funcionarios)
