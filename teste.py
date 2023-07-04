

import re 
import pprint

import main

def remove_incio_e_fim(lista):
    try:
        del lista[0]   # remover primeioro caractere
        lista.pop()
    except:
        ...

arquivo = open("log_meio_limpo.log","r")
tabelas = main.separete_tables(arquivo.readlines())
print(tabelas)
# lista_tuplas = [
#     (indice,valor)
#     for indice,valor in enumerate(lista_texto)
# ]

# dicionario = dict(lista_tuplas)
# # print(lista_tuplas)
# pprint.pprint(dicionario)
# arquivo.close()