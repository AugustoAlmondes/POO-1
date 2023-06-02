pessoas = {'Nome':[],'Endereco':[],'CEP':[],'Bairro':[],'Telefone':[]}

for i in range(10):
    nome = input("Digite o Nome: ")
    pessoas['Nome'].append(nome)

    endereco = input("Digite o Endereço: ")
    pessoas['Endereco'].append(endereco)

    cep = input('Digite o CEP: ')
    pessoas['CEP'].append(cep)

    bairro = input("Digite o Bairro: ")
    pessoas['Bairro'].append(bairro)

    telefone = input("Digite o Telefone: ")
    pessoas['Telefone'].append(telefone)

for j in range (9,-1,-1):
    print(pessoas['Nome'][j])
    print(pessoas['Endereco'][j])
    print(pessoas['CEP'][j])
    print(pessoas['Bairro'][j])
    print(pessoas['Telefone'][j])