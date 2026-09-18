from desafios.desafio036.classe036 import *

def main():
    p1 = Pix()

    finalizar_compra(Pix(), 1500)
    finalizar_compra(CartaoCredito(), 9540.55)
    finalizar_compra(Boleto(), 750.66)

if __name__ == '__main__':
    main()