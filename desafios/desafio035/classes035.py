from abc import ABC, abstractmethod


class Arquivo(ABC):

    def __init__(self, nome:str, ext:str, tam:int=0):
        self.nome = nome
        self._extencao = None
        self.tamanho = tam
        self.extencao = ext

    @abstractmethod
    def abrir(self):
        pass

    @property
    def extencao(self):
        return self._extencao

    @extencao.setter
    def extencao(self, ext:str):
        formatos = ['pdf', 'doc', 'docx']
        ext = ext.lower().strip()
        if ext in formatos:
            self._extencao = ext
        else:
            raise AttributeError("O Arquivo está em um formato não suportado")

    @property
    def nome_completo(self):
        return f"'{self.nome}.{self.extencao}' ({self.tamanho/1_000_000}MB)"

class PDF(Arquivo):

    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'pdf', tam)

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}' no Adobe Reader")


class DOC(Arquivo):
    
    def __init__(self, nome:str, tam:int):
        super().__init__(nome, 'docx', tam)

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}' no Microsoft Word")


def abrir_aquivo(arquivo):
    arquivo.abrir()