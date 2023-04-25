from main import (
    parse_html,organizar_impressao,
    informacoes_uteis)


keys_uteis = (
    "maquina",
    "nome_arquivo",
    "dimensao",
    "perfil_impressao",
    "data_hora_inicio",
)


lista_principal = list()
dict_temp = dict()

conteudo = parse_html("RIPLOG.HTML")
lista_impressao = organizar_impressao(conteudo)
lista_impressao_limpa = informacoes_uteis(lista_impressao)

for valores in lista_impressao_limpa:
    for indice,valor in enumerate(valores):
        chave = keys_uteis[indice]
        # print(chave, valor)
        dict_temp[chave] = None
        # print(dict_temp.keys())
    lista_principal.append(dict_temp)
    dict_temp.clear()

for valor in lista_impressao_limpa:
    for i,v in enumerate(valor):
        lista_impressao[i] =  v

print(lista_principal)