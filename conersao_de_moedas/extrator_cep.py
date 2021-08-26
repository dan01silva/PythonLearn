# -*- coding: utf-8 -*-
# Trabalhando com expressões regulares

import re # Regular Expression -- RegEx
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 Digitos + hífen (opcional) + 3 digitos
#o ? diz que aquele atributo aparece 1 ou 0 vezes (opcional)
padrao = re.compile("0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]") # Codificadores abaixo
padraov1 = re.compile("0123456789]{5}[-]?[0123456789]{3}") # Codificando quantas vezes a sequencia aparece
padraov2 = re.compile("0-9]{5}[-]?[0-9]{3}") # Codificando o Intervalo
padraov3 = re.compile("0-9]{5}[-]{0,1}[0-9]{3}") # Codificando o hifen opcional
busca = padraov3.search(endereco) # retorna o objeto Math ou NONE caso false
if busca:
    cep = busca.group()
    print(cep)


