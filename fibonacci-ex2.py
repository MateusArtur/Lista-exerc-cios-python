sequencia = [0,1]

for num in range(2, 52):
    soma = sequencia[num-1] + sequencia[num-2]
    sequencia.append(soma)

print(sequencia)

escolheNum = int(input("Qual número deseja verificar se pertence a sequência de fibonacci? "))

encontrado = False

for indice in sequencia:
    if indice == escolheNum:
        print(" o número ", escolheNum ," pertence a sequência de fibonacci!")
        encontrado = True
    else:
        continue

if encontrado == False:
    print("o número", escolheNum ," não pertence a sequência de fibonacci!")