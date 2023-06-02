def tamString(s):
    contador = 0
    for i in s:
        contador += 1
    return contador


palavra = input("Digite uma palavra: ")
tamanho = tamString(palavra)
print(tamanho)