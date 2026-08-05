from rich import print
from rich import inspect
from pip._internal.commands import inspect


class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id:int, nome:str = None, saldo:float = 0, chave:str = None):
        self._id = id # protegido (#)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        self.__hash = chave.encode()
        print(f'A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo')

    def __str__(self):
        #return f'A conta {self._id} de {self._titular} tem R${self.__saldo:,.2f} de __saldo'
        return f'Estudo atual da conta {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito: {self._titular} de {valor:,.2f} reais na conta {self._id}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor >= self.__saldo:
            print(f"Saque NEGADO de R$ {valor:,.2f} na conta {self._id}: SALDO INSUFICIENTE")
        else:
            self.__saldo -= valor
            print(f"Sacado: {self._titular} de {valor:,.2f} reais na conta {self._id}")





