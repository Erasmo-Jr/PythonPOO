from personagem_rpg import Guerreiro, Mago


def main():
    p1 = Guerreiro(nome="Kratos", vida=2000)
    p2 = Mago(nome="Merlin", vida=3000)

    p1.atacar(p2, forca=1000)
    p2.curar()


if __name__ == "__main__":
    main()