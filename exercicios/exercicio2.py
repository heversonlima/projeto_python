# exercicio com condicionais fi e else

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
 #considerar orem de precedencia
media = (nota1 + nota2) / 2

if media >= 7.0:
    print(f'Media: {media:.1f}\nConceito: Aprovado.')
else:
    print(f'Media: {media:.1f}\nConceito: Reprovado')