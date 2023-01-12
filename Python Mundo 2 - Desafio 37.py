# Neste desafio vamos fazer uma calculadora diferente, ela não calcula ela converte números em 
# bases númericas diferentes, o usuário insere um número decimal inteiro, o sistema pergunta
# pra qual base binária converter, podendo ser binário, octal ou hexadecimal

print('*' *30)
print("{'Python Mundo 2 - Desafio 37':^30}")
print('*' *30)

decimal = int(input('Digite um numero decimal inteiro'))

print('''Escolha para qual base numerica vc deseja converter
B para binario
O para octal
H para hexadecimal''')

conversao=input().lower()
if conversao =='b':
	binario=bin(decimal)
	print(f'O numero decimal {decimal} em binario corresponde a {binario[2:]}')

elif conversao=='o':
	octal=oct(decimal)
	print(f'O numero decimal {decimal} em octal corresponde a {octal[2:]}')
	
elif conversao=='h':
	hexa=hex(decimal)
	print(f'O numero decimal {decimal} em hexadecimal corresponde a {hexa[2:]}')
else:
	print('Opcao invalida')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)