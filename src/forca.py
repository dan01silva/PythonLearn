def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    letras_acertadas = ['_','_','_','_','_','_']
    

    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
               letras_acertadas[index] = letra
            index += 1

        print('Letras acertadas: {}'.format(letras_acertadas))
        letras_faltando = (letras_acertadas.count('_'))

        if(letras_faltando < 1):
            print('Parabéns não falta mais nenhuma letra')
        else:
            print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()