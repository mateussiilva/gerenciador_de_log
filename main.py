

import re
from setings import PATTERN_HTML,QUEBRA_LINHA


def remover_html(texto):
    REGEX = re.compile(PATTERN_HTML)
    REGEX2 = re.compile(QUEBRA_LINHA)
    novo_texto = re.sub(REGEX,"",texto)
    texto = re.sub(REGEX2,"",novo_texto)
    return texto

arquivo_html = open("RIPLOG.html","r")

listas = []
temp = []
for linha in arquivo_html.readlines():
    texto_limpo = linha
    
    temp.append(texto_limpo)
    if "</TABLE>\n" in texto_limpo:
        listas.append(temp[:])
        temp.clear()
        
with open("riplog.txt","w+") as file_txt:
    for lista in listas:
        for linha in lista:
            texto = remover_html(linha) + "\n"
            file_txt.write(texto)
        file_txt.write("\n\t\t -------------------")

    
        
# texto_limpo = re.sub(REGEX,"",texto)
# print(texto_limpo)
arquivo_html.close()

