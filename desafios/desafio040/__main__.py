from desafios.desafio040.classe040 import *

def main():
    u = [Usuario("José", "jjsilva@hotmail.com"), Usuario("Ana", "anaana@gmail.com")]
    a = [Aluno("Maria", "Administração", "3 ano")]

    exportar_dados(JSON(), u)

if __name__ == '__main__':
    main()