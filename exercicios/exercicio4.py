# media aritmetica usando funções

def lerNotas():
    nota = float(input('Informe sua primeira nota: '))
    return nota

def resultado(n1,n2):
    media=(n1+n2) / 2
    print(f'Primeira nota: {n1}')
    print(f'Segunda nota: {n2}')
    print(f'Media: {media}')
    if media >= 7.0:
        print ('\nAprovado')
    else:
        print('\nReprovado')


a = lerNotas()
b = lerNotas()
resultado(a, b)    


