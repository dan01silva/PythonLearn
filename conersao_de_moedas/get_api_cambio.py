# -*- coding: utf-8 -*-
import requests
import json

class Cambiodolarapi:   
    url_API = 'https://economia.awesomeapi.com.br/last/USD-BRL'

    
    
    res = requests.get(url_API)

    

    if(res.status_code == 200):
        print( 'Status 200 OK')

         #Manipulando o obj json para obj em python
        obj_resp = json.loads(res.text) 
        #Percorrendo obj USDBRL e pegando o valor do dolar
        for key, value in obj_resp['USDBRL'].items(): 
            if (key == 'bid'):
                cotacao = value
    else: 
        print("Status inválido: 404")

#print(res.headers)
#print(res.text)
#print(cambio)
