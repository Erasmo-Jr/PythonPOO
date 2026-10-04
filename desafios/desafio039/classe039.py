from abc import ABC, abstractmethod
import re


class Validador(ABC):

    @abstractmethod
    def validar(self, valor:str) -> bool:
        pass

class Usuario(Validador):
    def validar(self, valor: str) -> bool:
        regex = r'^[a-z0-9_]{5,20}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Email(Validador):
    def validar(self, valor: str) -> bool:
        regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False


class Senha(Validador):
    def validar(self, valor: str) -> bool:
        regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@!#$%?]).{8,}$'
        if re.fullmatch(regex, valor):
            return True
        else:
            return False



def validar_dado(validador: Validador, valor: str):
    resultado = validador.validar(valor)
    print(f"Valor: {valor} é valido? {'SIM' if resultado else 'NÃO'}")
