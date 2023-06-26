




# abrir arquivo e ler linhas 
elementos_inuteis = ("<!--\n","<style")


INCIO_CSS = "<style type=text/css>"
FIM_CSS = "</style>"
INCIO_TABELA = '<TABLE class="tab1" border="1" cellpadding="0" cellspacing="0" summary="">'
FIM_TABELA = '</TABLE>'


def get_linhas_for_array(name_file):
    list_lines = []
    arquivo = open(f"{name_file}","r+",encoding="utf-8")
    for indice,linhas in enumerate(arquivo.readlines()):
        if len(linhas) > 2:
            list_lines.append(linhas)
    arquivo.close()
    
    return list_lines


if __name__ == "__main__":
    linhas_arquivos = get_linhas_for_array("RIPLOG.txt")
    for indice,linhas in enumerate(linhas_arquivos):
        linha_limpa =  linhas.strip("\n")
        if linha_limpa ==  INCIO_TABELA:
            inicio = indice
        if linha_limpa == FIM_TABELA:
            fim = indice
            fim += 1
            
    for linha in linhas_arquivos[inicio:fim]:
        print(linha)


