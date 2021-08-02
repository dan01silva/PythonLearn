precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]
print( min(precos))

valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))

    # set e o nome da Lista em Python que não permite valores duplicados "{}"
    # tuple é o nome da lista imutável em Python "()"
    # lista em Python é dado a partir das chaves "[]" 
    

    colecao = {11122233344, 22233344455, 33344455566}
 
    colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!

    for cpf in colecao:
     print(cpf)

    #dictionary
    
    instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
    value = instrutores['Flavio']
    print(value )


    #List Comprehensions
    frutas = ["maçã", "banana", "laranja", "melancia"]
    lista = [fruta.upper() for fruta in frutas]
    print(lista)    

    inteiros = [1,3,4,5,7,8]
    quadrados = [n*n for n in inteiros]
    print(quadrados)


    # Aplique a expressão (numero) em cada item (numero) da lista (inteiros) caso a condição (if) cond seja satisfeita.
    inteiros = [1,3,4,5,7,9,12,15]
    pares = [numero for numero in inteiros if numero % 2 == 0 ]
    print(pares)

arquivo= open('palavras.txt', 'r')
arquivo.read()


    