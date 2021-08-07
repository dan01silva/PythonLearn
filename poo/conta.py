from poo.cliente import Cliente
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

    @staticmethod
    def codigo_banco() -> None:
        return {'BB': '001', 'Caixa':'104', 'Bradesco': '237' }


              

    def extrato(self):
        print('Saldo disponível: {}'.format(self.get_saldo, self.get_titular))

    def deposita(self, valor):
        self.saldo += valor
    
    def __pode_sacar(self, valor):
        saldo_mais_limite = self.__limite + self.__saldo
        return valor <= saldo_mais_limite

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.saldo -= valor
            print("Saque efetuado.")
        else:
            print("Saldo insuficiente.")

    def transfere(self, valor, destino):
        if(self.__pode_sacar(valor)):
            destino.deposita(valor)
            print("Transferência efetuada...")
        else:
            print("Saldo insuficiente...")
            