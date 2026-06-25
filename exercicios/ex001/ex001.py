# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome:str = ""
        self.idade:int = 0

    # Métodos de Intância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = input("QUal nome do Gafanhoto? ")
g1.idade = int(input("Qual idade do Gafanhoto? "))
print(g1.mensagem())