faturamentos = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
estados = ["SP","RJ","MG","ES","OUTROS"]

soma = float(0)

for indice in faturamentos:
    soma+= indice

porcentagens = []

calculo = 0

for valor in faturamentos:
    calculo = valor / soma * 100
    porcentagens.append(calculo)

print("faturamento total: ", soma)
print('Percentual de participação de faturamento por estados:')

for uf, porcentagem in zip(estados, porcentagens):
    print(uf," obteve ", '%.2f' % (porcentagem) + "%"," do valor total de faturamento.")
