from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def preparar(self):
        print("--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("--- Bebida Pronta ---")

    def ferver_agua(self):
        print("1. Fervendo água a 100 graus Celsius.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print("3. Servindo em xícara pequena.")


class Cha(BebidaQuente):
    def misturar(self):
        print("2. Infusionando folhas de chá na água quente.")

    def servir(self):
        print("3. Servindo em xícara de porcelana.")


class Leite(BebidaQuente):
    def misturar(self):
        print("2. Aquecendo e misturando o leite.")

    def servir(self):
        print("3. Servindo em caneca grande, já com café.")