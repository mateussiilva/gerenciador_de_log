from main import parse_html,organizar_impressao,create_log_txt




conteudo = parse_html("RIPLOG.HTML")
lista_impressao = organizar_impressao(conteudo)
create_log_txt(lista_impressao,"log.txt")