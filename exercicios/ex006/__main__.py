from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario


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

