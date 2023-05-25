
lista = [2,3,4,5,6]
resto = []
original = []



for x in lista:
    if x % 2 == 0 or x % 3 == 0:
        original.append(x)
    else:
        resto.append(x)


print(resto)
print (original)