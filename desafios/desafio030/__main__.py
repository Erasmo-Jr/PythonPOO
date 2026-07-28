from desafios.desafio030.classe030 import *

def main():
    c = Credencial()
    c.senha = str(input('Senha: '))
    print(c.senha)

    c.validar('Endre@')

if __name__ == "__main__":
    main()