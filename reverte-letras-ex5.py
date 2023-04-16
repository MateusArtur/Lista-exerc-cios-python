palavra = input("Digite uma palavra para ser invertida: ")
inverte = []
for letra in palavra:
    inverte.append(letra)

palavraInversa = ""
for indice in inverte[::-1]:
    palavraInversa+=indice

print("A palavra invertida é: ", palavraInversa)