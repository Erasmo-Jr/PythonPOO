from functools import singledispatch, singledispatchmethod


class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f"Não foi possivel analisar o valor {valor}")

    @analisar.register
    def _(self, valor: int):
        print (f"{valor} é um número inteiro")
    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é um número com ponto flutuante (Real)")
    @analisar.register
    def _(self, valor: str):
        print (f"{valor} é uma String")
    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f"{valor} é uma coleção de dados")
