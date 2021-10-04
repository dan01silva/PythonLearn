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
        fatia1 = self.cpf[:3]
        fatia2 = self.cpf[3:6]
        fatia3 = self.cpf[6:9]
        fatia4 = self.cpf[9:11]
        return(
            "{}.{}.{}-{}".format(
            fatia1,
            fatia2,
            fatia3,
            fatia4
            )
        )
    def __str__(self) -> str:
        return self.formata_cpf()