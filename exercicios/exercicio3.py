# trabalhando com laço while 

qtd=0
soma=0
media=0

valor = float(input('Digite um valor')) 

while valor > 0.0:
    soma = soma+valor
    qtd = qtd+1
    valor = float(input('Digite um valor'))  

media = soma / qtd
print(f'\nTotoal da soma: {soma}')     
print(f'Valores rigitados: {qtd}')     
print(f'Media dos valores: {media}')     