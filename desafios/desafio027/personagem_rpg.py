import random
from abc import ABC, abstractmethod
from rich.console import Console

console = Console()


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        golpe = random.choice(self.golpes)
        dano = random.randint(1, forca)
        console.print(
            f"[bold cyan]{self.nome}[/bold cyan]([green]{self.vida}[/green]) atacou "
            f"[bold yellow]{alvo.nome}[/bold yellow]([green]{alvo.vida}[/green]) com um "
            f"[magenta]{golpe}[/magenta] de força [red]{forca}[/red]"
        )
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida -= dano
        console.print(f"[bold yellow]{self.nome}[/bold yellow] recebeu dano de [bold red]{dano}[/bold red]!")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Pulo Giratório", "Cabeçada", "Chute Voador"]

    def curar(self):
        pontos = random.randint(10, 30)
        self.vida += pontos
        console.print(
            f"[bold cyan]{self.nome}[/bold cyan] grita de fúria e recupera "
            f"[bold green]{pontos} pontos[/bold green] de vida."
        )


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raio Arcano", "Explosão Mística"]

    def curar(self):
        pontos = random.randint(1, 10)
        self.vida += pontos
        console.print(
            f"[bold cyan]{self.nome}[/bold cyan] fez uma magia de cura e recuperou "
            f"[bold green]{pontos} pontos[/bold green] de vida."
        )