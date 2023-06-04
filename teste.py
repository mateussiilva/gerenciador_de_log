from main import parse_html,remover_texto_inutil,organizar_impressao
class GeradorLog:
    def __init__(self,path_arquivo) -> None:
        self.path_arquivo = path_arquivo
    

path = "RIPLOG.html"
linhas = parse_html(path)
for linha in linhas:
    print(remover_texto_inutil(text=linha))