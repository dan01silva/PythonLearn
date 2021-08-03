class Conta:

    #Construtor
    def __init__(self, numero, titular, saldo, limite) -> None:
        print('Chamando cobtrutor do objeto ... {}'.format(self))
        #referencia do obj
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('Saldo disponível: {}'.format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    
    