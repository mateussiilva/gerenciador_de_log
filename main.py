import re
import copy
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


def palavra_dentro_de_frase(texto,palavra):
    p = re.compile(fr"{palavra}") 
    resultado = re.search(p,texto)
    if resultado is None:
        return None
    else:
        return True


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
        if len(texto_sem_html):
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


def gerar_dicionario(vetor):
    return dict(vetor)


def limpar_tamnho(valor_string):
    texto = valor_string.rstrip(" in ").replace(",",".").strip(" ").split("x")
    # return list(map(texto,lambda i: float(i)))
    return [float(texto[0]),float(texto[1])]

def converter_polegada_para_centimetro(lista):
    return (lista[0] / 39.37 , lista[1] / 39.37)
