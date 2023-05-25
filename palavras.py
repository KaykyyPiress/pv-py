def combinar_strings(palavra1, palavra2):
    tamanho_maximo = max(len(palavra1), len(palavra2))
    palavra_resultante = ""
    for i in range(tamanho_maximo):
        if i < len(palavra1):
            palavra_resultante += palavra1[i]
        if i < len(palavra2):
            palavra_resultante += palavra2[i]
    return palavra_resultante

palavra1 = input("")
palavra2 = input("")
resultado = combinar_strings(palavra1, palavra2)
print(resultado)


