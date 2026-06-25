from rich import print, inspect



class Pessoa:
    def __init__(self, nome = '', idade= 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'{self.nome} acabou de fazer matricula!')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} começou a dar aula!')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'{self.nome} acabou de bater ponto!')


a1 = Aluno('Erasmo', 25, 'Engenharia de Software', 'T01')
a1.fazer_aniversario()
a1.fazer_matricula()
#inspect(a1, methods=True)

p1 = Professor('Guanabara', 37, 'Biologia', 'Mestre')
p1.fazer_aniversario()
p1.dar_aula()
#inspect(p1, methods=True)

f1 = Funcionario('Cláudia', 27, 'Secretaria Escolar', 'Secretaria')
f1.fazer_aniversario()
f1.bater_ponto()
#inspect(f1, methods=True)

