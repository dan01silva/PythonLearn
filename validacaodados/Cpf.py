#importanto lib do pypi
from typing import ValuesView
from validate_docbr import CPF

class Cpf:
    def __init__(self, doc) -> None:
        doc = str(doc)
        if self.valida_cpf(doc):
            self.cpf = doc
        else:
            raise ValueError("CPF Invalido")

    def valida_cpf(self, doc):
        if len(doc) == 11:
            validacao = CPF()
            return validacao.validate(doc)
        else:
            raise ValueError("Quantidade de digitos invalido")
    
    def formata_cpf(self):
       mask_cpf = CPF()
       return mask_cpf.mask(self.cpf)       
       pass
    def __str__(self) -> str:
        return self.formata_cpf()