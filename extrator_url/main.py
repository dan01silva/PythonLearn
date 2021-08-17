htp = 'https://'
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

#Separando a base e os parametros
indice_interrogacao = url.find('?')
url_base = url[ :indice_interrogacao]
#print(url_base)
url_parametro = url[indice_interrogacao + 1: ]
print(url_parametro)


# Buscando o valor dos parametros
param_busca = "moedaOrigem"
indice_parametro = url_parametro.find(param_busca)
indice_valor = indice_parametro + len(param_busca) + 1

print(param_busca)

print(indice_parametro)


indice_e_comercial = url.find("&", indice_valor)
print(indice_e_comercial)

#Buscando o valor da moeda
if indice_e_comercial == -1:     
        valor =  url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]

print(valor)