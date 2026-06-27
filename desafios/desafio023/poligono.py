from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(qtd_lados=4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(qtd_lados=1)  # convenção comum p/ círculo no diagrama
        self.raio = raio

    def perimetro(self):
        return 2 * 3.14159 * self.raio

    def area(self):
        return 3.14159 * self.raio ** 2