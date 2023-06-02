dicionario = {'Nome':[],'Volta1':[],'Volta2':[],'Volta3':[]}

for i in range(5):
    dicionario['Nome'].append(input("Nome do Corredor: "))
    dicionario['Volta1'].append(float(input("Primeira Volta: ")))
    dicionario['Volta2'].append(float(input("Segunda Volta: ")))
    dicionario['Volta3'].append(float(input("Terceira Volta: ")))

menor = 0
aux = 0
aux2 = 0
for i in range(5):
    if aux == 0:
        menor = dicionario['Volta1'][i]
        aux += 1
    if menor > dicionario['Volta1'][i]:
        menor = dicionario['Volta1'][i]
        aux2 = i
for i in range(5):
    if aux == 0:
        menor = dicionario['Volta2'][i]
        aux += 1
    if menor > dicionario['Volta2'][i]:
        menor = dicionario['Volta2'][i]
        aux2 = i
for i in range(5):
    if aux == 0:
        menor = dicionario['Volta3'][i]
        aux += 1
    if menor > dicionario['Volta3'][i]:
        menor = dicionario['Volta3'][i]
        aux2 = i

print("A menor volta foi feita por {} ao tempo de: {} seg".format(dicionario['Nome'][aux2],menor))

media1 = dicionario['Volta1'][0]+dicionario['Volta2'][0]+dicionario['Volta3'][0]
media1 = media1/5

media2 = dicionario['Volta1'][1]+dicionario['Volta2'][1]+dicionario['Volta3'][1]
media2 = media2/5

media3 = dicionario['Volta1'][2]+dicionario['Volta2'][2]+dicionario['Volta3'][2]
media3 = media3/5

media4 = dicionario['Volta1'][3]+dicionario['Volta2'][3]+dicionario['Volta3'][3]
media4 = media4/5

media5 = dicionario['Volta1'][4]+dicionario['Volta2'][4]+dicionario['Volta3'][4]
media5 = media5/5

print("Media do Corredor1: {:.2f}".format(media1))
print("Media do Corredor2: {:.2f}".format(media2))
print("Media do Corredor3: {:.2f}".format(media3))
print("Media do Corredor4: {:.2f}".format(media4))
print("Media do Corredor5: {:.2f}".format(media5))

if media1 < media2 and media1 < media3 and media1 < media4 and media1 < media5:
    print("O campeão é: {}".format(dicionario['Nome'][0]))

elif media2 < media1 and media2 < media3 and media2 < media4 and media2 < media5:
    print("O campeão é: {}".format(dicionario['Nome'][1]))

elif media3 < media2 and media3 < media1 and media3 < media4 and media3 < media5:
    print("O campeão é: {}".format(dicionario['Nome'][2]))

elif media4 < media2 and media4 < media1 and media4 < media3 and media4 < media5:
    print("O campeão é: {}".format(dicionario['Nome'][3]))

elif media5 < media2 and media5 < media1 and media5 < media3 and media5 < media5:
    print("O campeão é: {}".format(dicionario['Nome'][4]))