class Carteira:

    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.saldo:,.2f} na carteira"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError("Você não tem autorização para alterar o saldo desse jeito")