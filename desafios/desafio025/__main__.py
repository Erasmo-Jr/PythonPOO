from rich.console import Console
from rich.table import Table
from transportes import Moto, Caminhao, Drone


def main():
    dist = 50

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    console = Console()
    tabela = Table(title="Tabela de Fretes")

    tabela.add_column("Distância", style="cyan")
    tabela.add_column("Tipo", style="yellow")
    tabela.add_column("Frete", style="green")

    for entrega in viagem:
        tabela.add_row(
            f"{entrega.distancia}Km",
            type(entrega).__name__,
            entrega.calcular_frete()
        )

    console.print(tabela)


if __name__ == "__main__":
    main()