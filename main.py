

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
    with open(name_file, "w") as file:
        for valores in list_valores:
            for linha in valores:

                file.write(linha)
            file.write("\n\t\tNOVA IMPRESSÃO\n\n")

        
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
    indiceis_uteis = (0,2,6,8,16,18,30,56,60,72)
    for valores in lista_valores:
        for indice,valor in enumerate(valores):
            if indice in indiceis_uteis:    
                v = valor.rstrip('&nbsp')
                temp.append(v)
                # print(f"{indice} : {valor.rstrip('&nbsp')}")
        lista.append(temp[:])
        temp.clear()
    return lista

if __name__ == "__main__":
    conteudo = parse_html("RIPLOG.HTML")
    lista_impressao = organizar_impressao(conteudo)
    lista = informacoes_uteis(lista_impressao)
    dados = dict()
    for indice,valor in enumerate(lista):
        dados[f"{indice}"] = valor


    print(dados["0"])