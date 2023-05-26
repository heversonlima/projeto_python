class Main:
    pass
print('Testando...')

from Pessoa import Pessoa

pessoa1 = Pessoa("Heverson", "18", "Masculino")

print(pessoa1)
print(f'Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nGenero: {pessoa1.genero}')
