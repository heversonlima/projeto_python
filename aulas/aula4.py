# Condicionais

numA = int(input('digite um numero inteiro: '))
numB = int(input('digite um segundo numero inteiro: '))

if numA > numB:
    aux = numA
    numA = numB
    numB = aux
print(f'O valor da variavel A agora é: {numA}')
print(f'O valor da variavel B agora é: {numB}')