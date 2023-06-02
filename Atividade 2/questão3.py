palavra = input("Digite uma palavra: ")

procura = input("Digite um caracter: ")

contador = 0
for i in palavra:
    if(i == procura):
        print(contador)
    contador+=1