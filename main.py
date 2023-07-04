
import re


# abrir arquivo e ler linhas 
elementos_inuteis = ("<!--\n","<style")


INCIO_CSS = "<style type=text/css>"
FIM_CSS = "</style>"
INCIO_TABELA = '<TABLE class="tab1" border="1" cellpadding="0" cellspacing="0" summary="">'
FIM_TABELA = '</TABLE>'


def get_linhas_for_array(name_file):
    list_lines = []
    arquivo = open(f"{name_file}","r+")
    for indice,linhas in enumerate(arquivo.readlines()):
        if len(linhas) > 2:
            list_lines.append(linhas)
    arquivo.close()    
    return list_lines


def remove_html(text):
    p = re.compile(r'<.*?>')
    return re.sub(p,"",text)

def remover_caracteres_inuteis(text,char="&nbsp;"):
    p = re.compile(fr'{char}')
    return re.sub(p,"",text)

def separete_tables(vetor):
    lista_tabelas = []
    temp = []
    for indice,linha in enumerate(vetor):
        texto = linha.rstrip("\n\n")
        texto_sem_html = remover_caracteres_inuteis(remove_html(texto))
        if len(texto_sem_html) > 2:
            temp.append(texto_sem_html)
        if  texto == FIM_TABELA:
            lista_tabelas.append(temp[:])
            temp.clear()
    return lista_tabelas


def gravar_arquivo_log_principal(matrix,name_file):
    arquivo = open(f"{name_file}","w+")
    for vetores in matrix:
        for linha in vetores:
            texto_linha = linha + "\n"
            arquivo.write(texto_linha)
        arquivo.write("-------------------------\n")
    arquivo.close()
    return arquivo


def seprar_elementos_string(text,chars="&nbsp;"):
    lista_linha = text.split(chars)
    for indice,linha in enumerate(lista_linha):
        return linha

linhas_arquivo = get_linhas_for_array("RIPLOG.txt")
lista_tabelas_separadas = separete_tables(linhas_arquivo)
log_limpo = gravar_arquivo_log_principal(
    lista_tabelas_separadas,
    name_file="log_meio_limpo.log")


# for tabelas in lista_tabelas_separadas:
#     for tabela in tabelas:
#         texto = seprar_elementos_string(tabela)
#     print("-------------")