from desafios.desafio034 import *
from desafios.desafio034.classes034 import Desenvolvedor, Designer, Gerente


def main():
    funcionarios = [
        Desenvolvedor("Erasmo", 18_000),
        Designer("Raimundo", 25_000),
        Gerente("Vilian", 45_000),
    ]

    for f in funcionarios:
        print(f)

if __name__ == '__main__':
    main()