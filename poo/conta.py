from typing import get_args


class Conta:

    #Construtor
    def __init__(self, numero, titular, saldo, limite) -> None:
        print('Chamando cobtrutor do objeto ... {}'.format(self))
        #referencia do obj
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        ##__ torna o atributo privado 

    ## Getters e Setters
    
    def get_numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite


    

    def extrato(self):
        print('Saldo disponível: {}'.format(self.get_saldo, self.get_titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    