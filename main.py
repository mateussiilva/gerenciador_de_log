

import re

regex = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
PATTERN_HTML = re.compile(regex)

def parse_html(file) -> list:
    linhas = []
    with open(file,'r') as f:
        for linha in f.readlines():
            t = str(linha)
            if not len(t) == 1:
                linhas.append(t)
    return linhas

def create_log_txt(list_valores, name_file):   
    """Essa função cria um arquivo contendo as informções passadas como um vetor
        
    :param lista_valores -> uma lista contendo informações a serem gravados no arquivo
    :param name_file -> o nome do arquvio a ser criado
    
    """ 
    with open(name_file, "w") as file:
        for valores in list_valores:
            for linha in valores:
                file.write(linha)

        
def organizar_impressao(lista_valores):
    lista_impressao = []
    temp = [] 
    for linha  in lista_valores:
        texto = re.sub(PATTERN_HTML,"",linha)
        texto_novo = f"{remove_text(texto,char_remove='&nbsp')}"
        if not texto == "\n":
            temp.append(texto_novo)
        
        if linha == "</TABLE>\n":
            lista_impressao.append(temp[:])
            temp.clear()
          

    return lista_impressao

def remove_text(text,padrao=";",char_remove=""):
    lista_texto = text.split(padrao)
    for valor in lista_texto:
        if not valor.strip().lower() == char_remove:
            return str(valor)


def informacoes_uteis(lista_valores):
    lista = []
    temp = []
    indiceis_uteis = (2,6,18,32,62)
    for valores in lista_valores:
        for indice,valor in enumerate(valores):       
            v = valor.rstrip('&nbsp')
            
            if indice in indiceis_uteis:
                temp.append(v)

        lista.append(temp[:])
        temp.clear()
    return lista

if __name__ == "__main__":
    keys = ["nome_maquina","nome","ta"]
    conteudo = parse_html("RIPLOG.HTML")
    lista_impressao = organizar_impressao(conteudo)
    lista = informacoes_uteis(lista_impressao)
    arquivo = create_log_txt(lista_impressao, "log.log")