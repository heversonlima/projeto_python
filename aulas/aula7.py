import os
# laço de repetiçao for

#exemplo1
for n in range(10):
    print(n)

a = input('\nenter pro proximo exemplo')
os.system('cls') #limpando a tela

"""
    Por padrão, o valor inicial do laço de repetição é 0.
    Podemos alterar esse valor no comando range.
"""
#exemplo2
print('Selecionando em qual valor começar e terminar\n')
for n in range(5, 15):
    print(n)

a = input('\nenter pro proximo exemplo')
os.system('cls')

#exemplo3
print('Decremento de valores, ordem descrecente')

for n in range(10, 0, -1):
    print(n)


