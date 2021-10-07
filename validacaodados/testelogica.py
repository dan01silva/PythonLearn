from cpf_cnpj import CpfCnpj

from validate_docbr import CNPJ, CPF

    

#objeto_cpf = Cpf(42689614880)#objeto cpf
#print(objeto_cpf)

#cpf = CPF()
#print(cpf.validate("412.342.543-09"))  # True

#Teste CNPJ

cnpj = CNPJ()
cpf = CPF()



cnpj_cpf = CpfCnpj(cnpj.generate(), "cnpj")
cpf_cnpj = CpfCnpj(cpf.generate(), "cpf")


print("{} <<<<<>>>>> {} ".format(cnpj_cpf, cpf_cnpj) )