from abc import ABC, abstractmethod
from rich.console import Console
from rich.panel import Panel

console = Console()


class Funcionario(ABC):
    sal_min = 1612
    inss = 7.5

    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        qtd_sal_min = self.salario / self.sal_min
        texto = (
            f"O salário de [cyan]{self.nome}[/cyan] ([yellow]{type(self).__name__}[/yellow]) "
            f"é de [green]R${self.salario:.2f}[/green] e corresponde a "
            f"[magenta]{qtd_sal_min:.1f} salários mínimos[/magenta]."
        )
        console.print(Panel(texto, title="Análise de Salário"))


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, qtd_horas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calcular_salario(self):
        self.sal_bruto = self.valor_hora * self.qtd_horas
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        return self.salario


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.sal_bruto = salario_bruto

    def calcular_salario(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        return self.salario