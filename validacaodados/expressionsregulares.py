import re
from typing import TextIO

padrao = "[0-9]{2}[a-z][0-9]" #RE
padrao_cel = "[0-9]{11}"

texto = "124a33 1a2 1df ff3"

texto2 = "auiehfiehfa9hf11975741599ojfopejfoejfejf13034j34n3434=3434pn343-43nt95-40j4gm3404945hn480y4444420243"

resposta = re.search(padrao, texto)
resposta_cel = re.search(padrao_cel,texto2)
print(resposta)


