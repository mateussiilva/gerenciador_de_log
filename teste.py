
path = "RIPLOG.html"
linhas = parse_html(path)
for linha in linhas:
    print(remover_texto_inutil(text=linha))