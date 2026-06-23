
import os
import random


def desenhar_forca(erros):
    """
    Desenha a forca com base no número de erros cometidos.
    Cada erro adiciona uma nova parte ao desenho.
    """
    partes = [
        "     _______  ",
        "     |     | ",
        "     |     O ",
        "     |     | ",
        "     |     /\\",
        "     |    /  \\",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
        "     |         ",
    ]
    # Exibe apenas as partes correspondentes ao número de erros
    for i in range(erros):
        print(partes[i])
    print()

def selecionar_tema():
    """
    Exibe os temas disponíveis e permite que o jogador escolha um.
    Retorna o tema escolhido.
    """
    print("Bem-vindo ao Jogo da Forca!")
    print("Escolha um tema:")
    temas = {
        1: "Animais",
        2: "Objetos",
        3: "Comidas",
        4: "Frutas",
        5: "Cores"
    }
    for i, tema in temas.items():
        print(f"{i}. {tema}")
    # Lê a escolha do usuário até receber um valor válido
    while True:
        try:
            escolha = int(input("Digite o número do tema: "))
            if escolha in temas:
                return temas[escolha]
            else:
                print("Escolha inválida. Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite o número correspondente ao tema.")

def escolher_palavra(tema):
    """
    Seleciona uma palavra aleatória do tema escolhido.
    Retorna a palavra em minúsculas.
    """
    palavras = {
        "Animais": ["cachorro", "gato", "elefante", "macaco", "tigre"],
        "Objetos": ["cadeira", "mesa", "televisor", "computador", "telefone"],
        "Comidas": ["maçã", "banana", "pão", "sanduíche", "brigadeiro"],
        "Frutas": ["laranja", "uva", "manga", "morango", "kiwi"],
        "Cores": ["vermelho", "azul", "amarelo", "verde", "rosa"]
    }
    # Seleciona uma palavra aleatória do tema escolhido
    return random.choice(palavras[tema]).lower()

def jogar_forca():
    """
    Função principal que controla o fluxo do jogo.
    """
    tema = selecionar_tema()
    palavra = escolher_palavra(tema)
    letras_corretas = set()
    letras_erradas = set()
    tentativas_maximas = 6
    tentativas_restantes = tentativas_maximas
    
    while tentativas_restantes > 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nTema: {tema}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        desenhar_forca(len(letras_erradas))
        
        # Exibe o estado atual da palavra
        estado_palavra = [letra if letra in letras_corretas else "_" for letra in palavra]
        print(" ".join(estado_palavra))
        
        # Verifica se o jogador venceu
        if "_" not in estado_palavra:
            print("Parabéns! Você venceu!")
            return
        
        # Solicita chute do jogador
        chute = input("Chute uma letra: ").lower()
        
        # Validação do input
        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite uma letra válida.")
            continue
        
        if chute in letras_corretas or chute in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        # Atualiza o estado do jogo
        if chute in palavra:
            letras_corretas.add(chute)
        else:
            letras_erradas.add(chute)
            tentativas_restantes -= 1
    
    # Mensagem de derrota
    os.system('cls' if os.name == 'nt' else 'clear')
    desenhar_forca(len(letras_erradas))
    print(f"Você perdeu! A palavra era '{palavra}'.")
    print("Fim do jogo.")

if __name__ == "__main__":
    jogar_forca()