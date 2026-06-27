from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def calcular_frete(self):
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"


class Caminhao(Transporte):
    fator = 1.20

    def calcular_frete(self):
        if self.distancia < 50:
            return "Raio mínimo de 50Km"
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"


class Drone(Caminhao):
    fator = 9.50

    def calcular_frete(self):
        if self.distancia > 10:
            return "Raio máximo de 10Km"
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"