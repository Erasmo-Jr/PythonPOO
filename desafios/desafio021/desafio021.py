class Caneta:
    CORES = {
        'azul': '\033[34m',
        'vermelha': '\033[31m',
        'verde': '\033[32m',
        'amarela': '\033[33m',
        'preta': '\033[30m',
    }
    RESET = '\033[m'

    def __init__(self, cor='preta'):
        self.cor = cor
        self.tampada = True
        self.ponta = 1

    def destampar(self):
        self.tampada = False

    def tampar(self):
        self.tampada = True

    def escrever(self, texto):
        if self.tampada:
            print('A caneta está tampada. Destampe-a antes de escrever!')
            return
        cor_ansi = self.CORES.get(self.cor, self.RESET)
        print(f'{cor_ansi}{texto}{self.RESET}', end='')

    def quebrar_linha(self, quantidade=1):
        print('\n' * (quantidade - 1))


# Programa principal
c1 = Caneta('azul')
c2 = Caneta('vermelha')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Olá, tudo bem? ')
c1.quebrar_linha(2)
c2.escrever('Olá, Gafanhoto! ')
c3.escrever('Vamos exercitar!')