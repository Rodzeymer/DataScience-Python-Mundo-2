decimal = int(input('Digite um numero decimal inteiro'))

print('''Escolha para qual base numerica vc deseja converter
B para binario
O para octal
H para hexadecimal''')

conversao=input().lower()

if conversao =='b':
	binario=bin(decimal)
	print('O numero decimal {} em binario corresponde a {}'.format(decimal, binario[2:]))

elif conversao=='o':
	octal=oct(decimal)
	print('O numero decimal {} em octal corresponde a {}'.format(decimal, octal[2:]))
	
elif conversao=='h':
	hexa=hex(decimal)
	print('O numero decimal {} em hexadecimal corresponde a {}'.format(decimal, hexa[2:]))
else:
	print('Opcao invalida')