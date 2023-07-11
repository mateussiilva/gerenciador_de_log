

with open("mutoh_log_limpo.txt") as arquivo_log:
    lista_dados = []
    tmp = []
    linhas_arquvio = arquivo_log.readlines()

for linha in linhas_arquvio:
    tmp.append(linha.strip())
    if linha == "VJ-1604W (ValueJet)\n":
        lista_dados.append(tmp[:])
        tmp.clear()


soma = 0
for dados in lista_dados:
    for dado in dados:
        if "5/25/2022" in dado and "Trabalho de Impressão" in dados:
            metros = dados[7].rstrip("cm").split("x")
            maior_metro = float(max(metros))
            soma += maior_metro


print("Total de {}".format(soma /100))