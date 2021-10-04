# -*- coding: utf-8 -*-
import re
import requests
import json
import requests
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        
        if not self.url:
            raise ValueError("A URL esta vazia")

        padrao_url = re.compile('(https)?(://)(www.)?(bytebank.com)(.br)?(/cambio)')
        match = padrao_url.match(url)
        if not match:
            raise ValueError( ' A URL nao eh valida')

        print("A URL eh Valida")
        
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros   

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    #Realizando GET na API de cotacao
    url_API = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    res = requests.get(url_API)
    if res.status_code == 200 : 'Status 200 OK'
            #Manipulando o obj json para obj em python
    obj_resp = json.loads(res.text) 
            #Percorrendo obj USDBRL e pegando o valor do dolar
    for key, value in obj_resp['USDBRL'].items(): 
        if (key == 'bid'):
            cotacao = value    
        
    #Metodo especial
    def __str__(self):
        return f'URL: {self.url}\n URL base: {self.get_url_base()}\n Parametros: {self.get_url_parametros()}\n Cotacao do Dolar AGORA: {self.get_cotacao}'

    #Metodo especial
    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url


url = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#other = "https://www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
#valor_quantidade = extrator_url.get_valor_parametro("quantidade")
#print(valor_quantidade)
#print(f'Tamanho da URL: {len(extrator_url)}')
#print(extrator_url)


#print(extrator_url == extrator_url_1) #extrator_url.__eq__(extrator_url1)

#Verificando endere�o de mem�ria ID
#print(id(extrator_url))
#print(id(extrator_url_1))


#print(1 == True)
# Comparando o ID
#print(1 is True)
#print(bool("") is False)  


VALOR_DOLAR = extrator_url.cotacao  #return value realtime
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")