import random


def jogar():

    imprimir_msg_abertura()
    palavra_secreta = palavra_secreta_random()

    # Inicializando lista de acordo com quantidades de caracteres na palavra_secreta
    # List Comprehensions
    letras_acertadas = list_lestras_acertadas(palavra_secreta)

    # for letra in palavra_secreta:
    # letras_acertadas.append('_')

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print(letras_acertadas)

        chute = pede_chute()

        if(chute in palavra_secreta):
            confere_chute(palavra_secreta, letras_acertadas, chute)
        else:
            erros += 1
            desenha_forca(erros)
            
        enforcou = erros == 7

        acertou = "_" not in letras_acertadas

        print('Letras acertadas: {}'.format(letras_acertadas))
        letras_faltando = (letras_acertadas.count('_'))
        print('Ainda faltam {} letras'.format(letras_faltando))

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprimir_msg_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def palavra_secreta_random():
    # inicializando a list da palavra
    palavras = []

    # utilizando with não é necessário fehcar o fluxo (close()) o python cuida disso
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    # print(palavras)

    palavraRandom = random.randrange(0, len(palavras))

    palavra_secreta = palavras[palavraRandom].upper()

    return palavra_secreta


def list_lestras_acertadas(palavra):
    return ['_' for letras in palavra]


def confere_chute(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
