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
        linha.append(random.randint(0, 99))
    m.append(linha)

for linha in range(len(m)):
    for coluna in range (len(m[linha])):
        print("%3d" % m[linha][coluna], end="")
    print ()

"""tipo = str(input("S ou M: "))

if input.upper() == "S":
    for i in range(len(m)):
        for coluna in m[i]"""

for linha in range(len(m)):
    print(m[linha][0])