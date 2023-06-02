def troca(s):
    sl = list(s)
    print(f'separada por lista: {sl}')
    for x in range(0, len(sl)):
        for y in range(0, len(sl)):
            if sl[x] < sl[y]:
                aux = sl[x]
                sl[x] = sl[y]
                sl[y] = aux
    print(f'Forma Ordenada: {sl}')
    ls = ''.join(sl)
    print(f'Lista trasformada em String ordenada: {ls}')

palavra = str(input('Digite uma palavra: '))
troca(palavra)
