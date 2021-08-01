def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    # Inicializando lista de acordo com quantidades de caracteres na palavra_secreta
    letras_acertadas = ['_' for letras in palavra_secreta] ##List Comprehensions

    # Equivalente a interação acima.
    # for letra in palavra_secreta:
        # letras_acertadas.append('_')

    enforcou = False
    acertou = False
    erros = 0   
    

    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            
        enforcou = erros == 10 
       
        ##acertou = "_" not in letras_acertada

        print('Letras acertadas: {}'.format(letras_acertadas))
        letras_faltando = (letras_acertadas.count('_'))     
        print( 'Ainda faltam {} letras'.format(letras_faltando))     
        break
    if(acertou):
        print("Parabéns você ganhou")
    else:
        print("Suas chances acabaram, mas não desista")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()