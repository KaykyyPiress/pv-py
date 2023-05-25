"""matriz = []

for x in range(3):
    lista = []
    for y in range(3):
        num = int(input(""))
        lista.append(num)
    matriz.append(lista)

print(matriz)
"""

import random

m = []

for num_linha in range(12):
    linha = []
    for num_coluna in range(12):
        linha.append(num_linha+ num_coluna)
    m.append(linha)

for linha in range(len(m)):
    for coluna in range (len(m[linha])):
        print("%3d" % m[linha][coluna], end="")
    print ()


"""for i in range(12):
    linha = []
    for n in range(12):
        linha.append(random.randint(0,99))
    m.append(linha)

print("Matriz original: ")
for linha in range(len(m)):
    for coluna in range(len(m[linha])):
        print("%3d" % m[linha][coluna], end="")
    print()"""

soma = 0
for linha in range(7, 12):
    if linha == 7:
        soma += m[7][5]
        soma += m[7][6]
    elif linha == 8:
        for n in range(8, 12):
            if linha == 8:
                for x in range (4, 8):
                    soma += m[8][x]
                
                
print(soma)




    

