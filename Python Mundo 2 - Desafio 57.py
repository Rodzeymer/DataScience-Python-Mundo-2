# No último desafio foi incluso no final do código umas instruções para validar se o grupo
# tinha ou não homens, então nete desafio vamos criar um validador de sexo simples, em que o
# programa irá continuar no looping enquanto o usuário não inserir o que  foi pedido, que
# indique o sexo entre M ou F, qualquer outra entrada será rejeitada e o algorimo perguntará
# de novo pelo sexo até que seja inserido M ou F

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 57':^30}")
print('*' *30)

sexo = 'k'

while sexo not in 'MF':
    sexo = str(input('Digite o seu sexo [M/F]')).upper()
    if sexo in 'MF':
        print(f'Sexo {sexo} é válido')
    else:
        print(f'Sexo {sexo} não é válido')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)