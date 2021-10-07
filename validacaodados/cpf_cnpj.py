#importanto lib do pypi
from typing import ValuesView
from validate_docbr import CNPJ, CPF

class CpfCnpj:
    def __init__(self, doc, tipo_doc) -> None:
        doc = str(doc)
        self.tipo_doc = tipo_doc

        if  self.tipo_doc == "cpf":
            if self.valida_cpf(doc):
                self.cpf = doc
            else:
                raise ValueError("CPF Invalido!!")
        elif self.tipo_doc =="cnpj": 
            if self.valida_cnpj(doc):
                self.cnpj = doc  
            else:
                raise ValueError("CNPJ Invalido")
        else:
            raise ValueError("Documento invalido")

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
        if  self.tipo_doc == "cpf":
            return self.formata_cpf()
        elif self.tipo_doc == "cnpj":
            return self.formata_cnpj()
    
    def valida_cnpj(self,cnpj):
        if len(cnpj) == 14:
            validacao_cnpj = CNPJ()
            return validacao_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos invalido")

    def formata_cnpj(self) -> None:
        mask_cnpj = CNPJ()
        return mask_cnpj.mask(self.cnpj)
