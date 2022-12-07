from classes import Cliente, Funcionario
from user import user
from admin import admin
from proletario import proletario
from random import randint

def caixa_de_texto(string):
    print("\n", "-" * 50, "\n", " " * ((50-len(string))//2), string, "\n", "-" * 50)


with open("nomes.txt", 'r', encoding='utf-8') as arquivo:
    nomes = [nome.strip() for nome in arquivo]

clientes, funcionarios = [], []

for iteracao in range(50):
    clientes.append(Cliente(nomes[randint(0, len(nomes))-1], randint(100000000000, 999999999999), clientes,
                            randint(1000, 9999)))
    funcionarios.append(Funcionario(nomes[randint(0, len(nomes)) - 1], randint(100000000000, 999999999999), "cargo",
                                randint(1000, 9999), funcionarios))

caixa_de_texto("Bem-vinde ao Banco Budang")
print("Os números das contas variam entre 0 e 49.\n"
      "A senha (acesso cliente) é um PIN de 4 dígitos gerado aleatoriamente e revelada em caso de erro (modo dev).")
opt = int(input("\n1 - User\n2 - Admin\n3 - Funcionário\nSelecione um dos modos de operação (1,2 ou 3): "))

if opt == 1:
    user(clientes)
elif opt == 2:
    admin(clientes, funcionarios)
elif opt == 3:
    proletario(funcionarios)
else:
    print("Opção inválida, encerrando o programa.")
    exit()
