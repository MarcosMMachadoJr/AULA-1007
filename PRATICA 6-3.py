numeros = []

for cont in range(5):
    numeros.append(int(input("Digita um numero aí: ")))
    print()

for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        numeros[i] = 0

for n in numeros:
    print(n)