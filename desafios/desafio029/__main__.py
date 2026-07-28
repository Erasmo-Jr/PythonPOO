from rich import print, inspect
from desafios.desafio029.classes029 import Diario

def main():
    meudiario = Diario()
    meudiario.escrever("Essa é a primeira mensagem")
    meudiario.escrever("Estou aprendendo Python")
    try:
        meudiario.ler('Ejr@')
    except Exception as e:
        print(f"[red]ERRO: {e}")

    #inspect(meudiario, private=True)

if __name__ == "__main__":
    main()