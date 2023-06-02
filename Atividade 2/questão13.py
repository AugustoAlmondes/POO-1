def consultarTelefone(nome):
    return agenda[nome]

def excluirNome(nome):
    agenda.pop(nome)

def excluirTelefone(nome, tel):
    lista = agenda[nome]
    lista.remove(tel)
    agenda[nome] = lista
    if agenda[nome] == []:
        agenda.pop(nome)

def incluirTelefone(nome, tel):
    aux2 = 0
    for i in agenda:
        if i == nome:
            aux2 = 1
        if aux2 > 0:
            lista = agenda[nome]
            lista.append(tel)
            agenda[nome] = lista
    if aux2 == 0:
        opcao = int(input("1 - Sim\n2 - Não\nQuer adicionar este numero: "))
        if opcao == 1:
            incluirNovoNome(nome,tel)
        elif opcao == 2:
            return 0

def incluirNovoNome(nome, tel):
    lista = []
    lista.append(tel)
    agenda[nome] = lista

agenda = {}
aux = 0

while aux >= 0:
    aux = int(input('\n-1 - para sair\n'
        '1 - Incluir Novo Nome\n'
    '2 - Incluir Telefone\n'
    '3 - Excluir Telefone\n'
    '4 - Excluir Nome\n'
    '5 - Consultar Telefone\n'
    'Escolha uma das seguintes opções: '))

    if aux == 1:
        print("\nIncluir Nome")
        nome = input("Digite o Nome: ")
        tel =input("Digite o Telefone: ")
        incluirNovoNome(nome,tel)
    if aux == 2:
        print("\nIncluir Telefone")
        nome = input("Digite o Nome: ")
        tel = input("Digite o Telefone: ")
        incluirTelefone(nome,tel)
    if aux == 3:
        print("\nExcluir Telefone")
        nome = input("Digite o Nome: ")
        tel = input("Digite o Telefone: ")
        excluirTelefone(nome,tel)
    if aux == 4:
        print("\nExcluir Nome")
        nome = input("Digite o Nome: ")
        excluirNome(nome)
    if aux == 5:
        print("\nConsultar Agenda")
        nome = input("Digite o Nome: ")
        consultarTelefone(nome)
   