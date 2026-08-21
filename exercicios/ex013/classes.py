class Mae:
    def __init__(self, nome:str = 'mamãe'):
        self.nome = nome

    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM com com leite condensado e calda")

    def fritar_coxinha(self):
        print(f"{self.nome} frita COXINHA no óleo de soja")


class Filha(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} faz PUDIM comLeite Ninho e Nutella")

class Filho(Mae):
    def fritar_coxinha(self):
        print(f"{self.nome} frita COXINHA na Air Fryer")