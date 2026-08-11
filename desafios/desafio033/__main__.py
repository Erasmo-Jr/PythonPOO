from desafios.desafio033.classe033 import *

def main():
    a = Aluno("Erasmo", 2001, "ENG")

    a.add_curso("ENG")

    print(a.cursos_oficiais)
    print(a.__dict__)

if __name__ == '__main__':
    main()