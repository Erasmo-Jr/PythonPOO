from rich import print
from rich.panel import Panel
from rich import inspect

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos=sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Nome real: [black on blue] {self.nome} [/]'
        conteudo += f'\n Jogos favoritos:'
        for num, game in enumerate(self.favoritos):
            conteudo += f'\n:video_game: [blue]{game}[/]'
        painel = Panel(conteudo, title=f"[yellow]Jogador <{self.nick}>[/]", width=40)
        print(painel)


j1 = Gamer(nome="Erasmo Junior", nick="Endre")
j1.add_favoritos("FC26")
j1.add_favoritos("Dragon Ball Sparking Zero")
j1.add_favoritos("GTA5")
j1.add_favoritos("God of War")
j1.add_favoritos("Tomb raider")

j1.ficha()

