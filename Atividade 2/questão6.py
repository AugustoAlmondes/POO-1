lista=[]

print("Digite 10 numero")
for i in range(10):

    x = int(input())

    lista.append(x)

print(lista)

lista.reverse()

print("Reverso")
print(lista)