from desafios.desafio035.classes035 import *
from rich import print, inspect

def main():
    a1 = DOC('teste', 1200000)
    a2 = PDF("contrato", 850000)
    #inspect(a1, methods=True)
    abrir_aquivo(a1)
    abrir_aquivo(a2)

if __name__ == '__main__':
    main()