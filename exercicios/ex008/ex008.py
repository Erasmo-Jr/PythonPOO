from rich import print
from rich import inspect
from pip._internal.commands import inspect


class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo')

    def __str__(self):
        #return f'A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo'
        return f'Estudo atual da conta {self.__dict__}'

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito: {self.titular} de {valor:,.2f} reais na conta {self.id}")

    def sacar(self, valor):
        if valor >= self.saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE")
        else:
            self.saldo -= valor
            print(f"Sacado: {self.titular} de {valor:,.2f} reais na conta {self.id}")





