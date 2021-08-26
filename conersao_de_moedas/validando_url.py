import re

url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile('(https)?(://)(www.)?(bytebank.com)(.br)?(/cambio)')
match = padrao_url.match(url) # Natch verifica se a URL inteira é igual ao pdrão
if not match:
    raise ValueError( ' A URL nao eh valida')
print("A URL eh Valida")