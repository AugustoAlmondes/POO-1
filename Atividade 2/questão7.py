lista1 = []
lista2 = []
lista3 = []
print("Digite os numero da primeira lista:")
for i in range(10):
    x = int(input())
    lista1.append(x)

print("Digite os numero da segunda lista:")
for i in range(10):
    x = int(input())
    lista2.append(x)

print(lista1)
print(lista2)

for i in range (10):
    valor = lista1[i] * lista2[i]
    lista3.append(valor)

print(lista3)