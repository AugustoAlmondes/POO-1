dicionario = {'Nome':[],'Nota1':[],'Nota2':[]}
nome = 'Sei la'
for i in range(3):
    dicionario['Nome'].append(input("Digite o Nome: "))
    dicionario['Nota1'].append(int(input("Digite a primeira Nota: ")))
    dicionario['Nota2'].append(int(input("Digite a segunda Nota: ")))

while nome != '0':
    nome = input("Digite 0 para sair\nDigite o Nome para verificar a Media: ")
    for i in range(3):
        if nome == dicionario['Nome'][i]:
            media = dicionario['Nota1'][i]+dicionario['Nota2'][i]
            media = media/2
    print("A media é: {}".format(media))