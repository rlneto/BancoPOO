from collections.abc import Container
from datetime import datetime
from random import randint


class Pessoa:
    def __init__(self, nome, cpf):
        self._nome = nome.title()
        self._cpf = cpf

    def saque(self, valor):
        pass
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf


class Transacao():
    def __init__(self, tipo, valor, origem=None, destino=None):
        self._origem = origem
        self._destino = destino
        self._data = (datetime.today()).strftime('%d/%m/%Y %H:%M')
        if tipo == 0:
            self._tipo = 'Saque'
        elif tipo == 1:
            self._tipo = 'Depósito'
        elif tipo == 2:
            self._tipo = 'Transferência'
        elif tipo == 3:
            self._tipo = 'Empréstimo'
        else:
            self._tipo = 'Op Inválida'
        self._valor = valor

    def __str__(self):
        return f'\nDADOS DA TRANSAÇÃO\nData e hora: {self._data} \nConta de origem:{self._origem}\n' \
               f'Conta destino:{self._destino}\nTipo da operação: {self._tipo}\nValor: {self._valor} R$'


class Cliente(Pessoa, Container):

    def __init__(self, nome, cpf, cadastro, senha):
        super().__init__(nome, cpf)
        self._limite = 1000.0
        self._conta = len(cadastro)
        self._transacoes = []
        self._saldo = float(randint(0, 1000))
        self._senha = int(senha)

    def __contains__(self, item):
        return item in self.nome

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, novo_limite):
        self._limite = novo_limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def conta(self):
        return self._conta

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    def saque(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            if len(self._transacoes) > 11:
                self._transacoes.pop(0)
            self._transacoes.append(Transacao(0, -valor))
            print(self._transacoes[-1])
            return True
        else:
            print("Operação não realizada, saldo insuficiente.")
            return False

    def deposito(self, valor, origem):
        self.saldo += valor
        if len(self._transacoes) > 11:
            self._transacoes.pop(0)
        self._transacoes.append(Transacao(1, valor))
        print(self._transacoes[-1])

    def transferencia(self, destino, valor, cadastro):
        if destino < len(cadastro):
            if valor < self.saldo:
                self.saldo -= valor
                cadastro[destino].deposito(valor, self._conta)
                if len(self._transacoes) > 11:
                    self._transacoes.pop(0)
                self._transacoes.append(Transacao(2, -valor, self._conta, destino))
                print(self._transacoes[-1])
            else:
                print("Operação cancelada: Saldo insuficiente.")
        else:
            print("Operação cancelada: Conta inexistente.")

    def emprestimo(self, valor):
        if valor > self._limite:
            print("Você já utilizou seu limite de crédito.")
        else:
            self.saldo += valor
            self._limite -= valor
            if len(self._transacoes) > 11:
                self._transacoes.pop(0)
            self._transacoes.append(Transacao(3, valor))
            print(f"Empréstimo realizado com sucesso. Novo saldo: {self.saldo} R$")

    def extrato(self):
        print("\nRelação das últimas 10 operações realizadas.")
        for registro in self._transacoes:
            print(f'{self._transacoes.index(registro) + 1}:\n ', registro)

    def __str__(self):
        return f'\nDADOS DA CONTA\nTitular: {self.nome}\nConta Corrente: {self.conta}\nCPF: {self.cpf}\n' \
               f'Saldo: {self.saldo} R$\nLimite de crédito: {self.limite} R$'


class Funcionario(Pessoa):

    def __init__(self, nome, cpf, cargo, salario, cadastro):
        super().__init__(nome, cpf)
        self._cargo = cargo
        self._salario = salario
        self._numero = len(cadastro)
        self._saldo = salario

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def salario(self):
        return self._salario

    def saque(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} R$ realizado com sucesso.")
            print(self)
        else:
            print("Operação não realizada, saldo insuficiente.")

    def __str__(self):
        return f'\nDADOS DO FUNCIONÁRIO\nNome: {self.nome}\nNúmero: {self._numero}\nCPF: {self.cpf}\n' \
               f'Cargo: {self._cargo}\nSalário: {self._salario} R$\nSaldo em conta: {self.saldo} R$'
