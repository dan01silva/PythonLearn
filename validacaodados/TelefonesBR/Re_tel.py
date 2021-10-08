import re

class TelefonesBr():
    def __init__(self,telefonebr) -> None:
        
        if self.valida_tel(telefonebr):
            self.numero = telefonebr
        else:
            raise ValueError("Numero de telefone nao encontrado")
 
    def valida_tel(self, telefonebr):

        padrao_telefone = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        valida = re.findall(padrao_telefone, telefonebr)
        if valida:
             return True
        else:
            return False
    
    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})([0-9]{4})"  # "?" indica que aquele grupo não é obrigatorio
        resposta = re.search(padrao, self.numero)
        numero_formatado = "+({})({}){}-{}".format(
            resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
        return numero_formatado

    def __str__(self) -> str:
        return self.format_numero()