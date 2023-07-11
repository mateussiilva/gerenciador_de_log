from bs4 import BeautifulSoup





def separar_tabelas(arquivo_html,indices_validos) -> list:
    matrix_de_dados = []
    tmp = []
    with open(arquivo_html, "r",encoding="latin-1") as html_file:
        conteudo = html_file.read()
    soup = BeautifulSoup(conteudo,"html.parser")
    for dados in soup.findAll("table"):
        for indice,valor in enumerate(dados.find_all("td")):
            txt = valor.get_text().strip()

            
            tmp.append(txt)
        matrix_de_dados.append(tmp[:])
        tmp.clear()
    return matrix_de_dados



if __name__ == "__main__":
    name_file = "mutoh_log_limpo.txt"
    indices_validos = (0,2,5,8,16,30,33,35,37)
    tabelas_separadas = separar_tabelas("MUTOH.html",indices_validos)
    with open(name_file,"w+") as log_limpo:
        for tabela in tabelas_separadas:
            for info in tabela:
                l = info + "\n"
                log_limpo.write(l)
            log_limpo.write(",?\n")
    

