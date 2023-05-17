

import re

regex = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
PATTERN_HTML = re.compile(regex)

def parse_html(file) -> list:
    """ 
    Recebo uma uma arquivo, abro ele percorro cada linha dele identificando se o tamanho é diferente
    de 1 se for eu adiciono essa linha na minha lista e a retorno no final
    para
    
    """
    linhas = []
    with open(file,'r') as f:
        for linha in f.readlines():
            if not len(linha) == 1:
                linhas.append(linha)
    return linhas


def remover_texto_inutil(text,padrao=";",char_remove=""):
    lista_texto = text.split(padrao)
    for valor in lista_texto:
        if not valor.strip().lower() == char_remove:
            return str(valor)


def criar_arquivo_txt(list_valores, name_file):   
    """Essa função cria um arquivo contendo as informções passadas como um vetor
    :param lista_valores -> uma lista contendo informações a serem gravados no arquivo
    :param name_file -> o nome do arquvio a ser criado
    
    """ 
    with open(name_file, "w") as file:
        for valores in list_valores:
            for linha in valores:
                file.write(linha)
            file.write("\n\n")
        
def organizar_impressao(lista_valores):
    lista_impressao = []
    temp = [] 
    for linha  in lista_valores:
        
        texto = re.sub(PATTERN_HTML,"",linha)    
        texto_novo = f"{remover_texto_inutil(texto,char_remove='&nbsp')}"
        if not texto == "\n":
            temp.append(texto_novo)        
        if linha == "</TABLE>\n":
            lista_impressao.append(temp[:])
            temp.clear()
          
    return lista_impressao



if __name__ == "__main__":
    keys = ["nome_maquina","nome","ta"]
    conteudo = parse_html("RIPLOG.txt")
    lista_impressao = organizar_impressao(conteudo)
    arquivo = criar_arquivo_txt(lista_impressao, "log.log")
