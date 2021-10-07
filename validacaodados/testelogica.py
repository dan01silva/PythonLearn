from cpf_cnpj import Documento
from validate_docbr import CNPJ, CPF

#objeto_cpf = Cpf(42689614880)#objeto cpf
#print(objeto_cpf)

#cpf = CPF()
#print(cpf.validate("412.342.543-09"))  # True

#Teste CNPJ

cnpj = CNPJ()
cpf = CPF()


cnpj_cpf = Documento.cria_documento(cnpj.generate())

cpf_cnpj = Documento.cria_documento(cpf.generate())


print("{} <<<>>> {}".format(cnpj_cpf,cpf_cnpj) )