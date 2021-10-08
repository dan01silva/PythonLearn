import re
from Re_tel import TelefonesBr

padrao_email = "\w{2,50}@[a-z]{2,10}.[a-z]{2,3}.[a-z]{1,2}"
texto = "dnfineinvfb4897bgu4u4 4ur 44 fjnrg h48 gsjkdpfaj 8f f danielzsmattos@gmail.com.brbreofepge"
expression = re.search(padrao_email, texto)
print(expression)



padrao_ex = "(xx)xxxxx-xxxx"
padrao_telefone = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
texto1 = "Oi td bom ?, segue meu numero de telefonee 11975741599 gkfndfipbbffbpjob 21404849403 e tambem segue nimero do meu gestore\
    e tambem onumero do meu gestor o claudio onorio 05511495045003"
#resposta = re.search(padrao_telefone, texto1)
#print(resposta.group(2))

telefone = "5511975741599"

validando_telefone = TelefonesBr(telefone)
print(validando_telefone)

