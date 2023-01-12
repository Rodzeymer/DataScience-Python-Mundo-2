# Agora, como não poderia faltar, um desafio clássico, usando if e elif, o usuário é convidado
# a inserir dois números inteiros e o sistem avalia qual número é maior, simples?

print('*' *30)
print("{'Python Mundo 2 - Desafio 38':^30}")
print('*' *30)

numero1 = int(input('Digite o primeiro valor'))
numero2 = int(input('Digite o segundo valor'))

if numero1 > numero2:
    print(f'O primeiro valor: {numero1} é maior que o segundo: {numero2}')
elif numero2 > numero1:
    print(f'O segundo valor: {numero2} é maior que o primeiro: {numero1}')
else:
    print(f'Os valores são iguais {numero1} e {numero2}')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)