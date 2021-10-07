#importanto lib do pypi
from typing import ValuesView
from validate_docbr import CNPJ, CPF

class Documento:
#Facture
    @staticmethod
    def cria_documento(doc):
        if len(doc) == 11:
            return DocCpf(doc)
        elif len(doc) == 14:
            return DocCnpj(doc)

class DocCpf:
    def __init__(self, documento) -> None:
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido!!!!")

    def valida(self,doc):
        validacao = CPF()
        return validacao.validate(doc)

    def format(self):
        mask_cpf = CPF()
        return mask_cpf.mask(self.cpf)

    def __str__(self) -> str:
        return self.format()
class DocCnpj:
    def __init__(self, doc) -> None:
        if self.valida(doc):
            self.cnpj = doc
        else:
            raise ValueError("CNPJ invalido!!!!")

    def valida(self,doc):
        validacao_cnpj = CNPJ()
        return validacao_cnpj.validate(doc)
    
    def format(self):
        mask_cnpj = CNPJ()
        return mask_cnpj.mask(self.cnpj)

    def __str__(self) -> str:
        return self.format()             