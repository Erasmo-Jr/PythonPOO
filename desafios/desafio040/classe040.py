class Usuario:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Aluno:

    def __init__(self, nome, curso, serie):
        self.nome = nome
        self.curso = curso
        self.serie = serie

class JSON:

    def exportar(self, dados):
        from json import dumps

class XML:

    def exportar(self, dados):
        return f"Exportando dados de {dados} para XML"

def exportar_dados(formato, dados):
    print(formato.exportar(dados))

