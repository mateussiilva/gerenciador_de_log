

import re




regex = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
PATTERN_HTML = re.compile(regex)



def parse_html(file) -> list:
    linhas = []
    with open(file,'r') as f:
        for linha in f.readlines():
            t = str(linha)
            # text = re.sub(PATTERN_CSS,"",t)
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
    for indice,linha  in enumerate(lista_valores):
        texto = re.sub(PATTERN_HTML,"",linha)
        if not texto == "\n":
            temp.append(texto)
        
        if linha == "</TABLE>\n":
            lista_impressao.append(temp[:])
            temp.clear()

    return lista_impressao


conteudo = parse_html("RIPLOG.HTML")
lista_impressao = organizar_impressao(conteudo)
create_log_txt(lista_impressao,"log.txt")
