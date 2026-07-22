from exercicios.ex009.ex009 import Avaliacao
from rich import print, inspect


def main():
    av1 = Avaliacao("Pedro", "Matemática", 9.5)
    inspect(av1)

if __name__ == "__main__":
    main()