from main import *
import pprint


linhas_arquivo = get_linhas_for_array("tex.txt")
lista_tabelas_separadas = separete_tables(linhas_arquivo)

tabelas = lista_tabelas_separadas
tabelas_impressoes = []

for indice,tabela in enumerate(tabelas):
    if  "RIP" not in tabela[0]:
        tabelas_impressoes.append(tabela)


lista_impressao_tuplas = []
tmep = []
for impressao in tabelas_impressoes:
    for ind,imp in enumerate(impressao):
        valores = (ind,imp)
        tmep.append(valores)
    dicionario_impressao = gerar_dicionario(tmep)
    lista_impressao_tuplas.append(copy.deepcopy(dicionario_impressao))
    dicionario_impressao.clear()
    tmep.clear()

# print(len(lista_impressao_tuplas))

nome = 6
tamanho = 16
data = 64
data_inicial = "2023"
# resultado = lista_impressao_tuplas[1]
# pprint.pprint(resultado.get(data))


soma = 0
for impressao in lista_impressao_tuplas:
    try:
        result = impressao.get(data)
        result_texto = str(result)
    except:
        ...
    if result is not None and data_inicial in result:
        t = converter_polegada_para_centimetro(
            limpar_tamnho(impressao.get(tamanho)))
        soma += t[1]
        
        print(f"nome:{impressao.get(nome)}\ntamanho:{t}")
print(f"Total de {soma:.2f} metros")