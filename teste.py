import os
from setings import CAMINHO_LOG_TXT
import re
from main import remover_texto_inutil

def criar_arquivo(nome_arquivo,dados=" "):
    try:
        with open(nome_arquivo,'w+') as file:
            ...
    except:
        ...
pattern = r'<.*?>'
regex = re.compile(pattern)
def converter_para_txt(caminho_arquivo):
    try:
        with open(caminho_arquivo,"r") as file, open("log.txt",'w+') as \
            new_file:
            nome = "log.txt"        
            for linha in file.readlines():
                linha_limp = linha
                new_file.write(linha_limp)
            
        ret = (True,os.path.abspath(nome))
    except Exception as e:
        print(e)
        ret = (False,None)
    
    return ret
# converter_para_txt("RIPLOG.txt")

impressoes = []
temp = []
with open(CAMINHO_LOG_TXT,'r') as file:
    for posicao,linha in enumerate(file.readlines()):
        if len(linha) >2:
            temp.append(linha)
        if linha == "</TABLE>\n":
            impressoes.append(temp[:])
            temp.clear()
    
    
arquivo = criar_arquivo("log_limpo.txt")
file = open("log_limpo.txt","w")
for impressao in impressoes:
    for informacao in impressao:
        texto = re.sub(regex,"",informacao)
        t = remover_texto_inutil(texto)
        file.write(texto.rstrip("\n"))
    sep = "-"*50 +"\n"
    file.write(sep)