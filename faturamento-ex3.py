import json

with open("Projetos_pessoais/exercicios/dados.json") as dados:
    faturamento = json.load(dados)

def armazenaValores():
    porDia =[]

    for indice in faturamento:
        if indice["valor"] != 0.0:
            porDia.append(indice["valor"])
    print("O menor dia em faturamento neste mês acumulou R$","%.2f"% (min(porDia)))
    print("O maior dia em faturamento neste mês acumulou R$","%.2f"% (max(porDia)))
    return porDia

def calculaMedia(porDia):
    dividendo = sum(porDia)
    divisor = len(porDia)
    media = dividendo/divisor
    print("A média de faturamento diário foi R$","%.2f"% (media))
    return media

def CalculadiasAcimaMedia(porDia, media):
    diasAcimaDaMedia = []

    for valor in porDia:
        if valor > media:
            diasAcimaDaMedia.append(valor)
    print("Neste mês tivemos ", len(diasAcimaDaMedia) ," dias acima da média de faturamento.")

porDia = armazenaValores()
media = calculaMedia(porDia)
CalculadiasAcimaMedia(porDia, media)
