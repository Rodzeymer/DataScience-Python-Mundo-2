# Neste desafio foi construído um algoritmo que identifica se o número informado pelo usuário é
# ou não primo, já que um número primo possui apenas dois divisores de resto zero, o 1 e ele
# mesmo, o programa verifica quantos divisores que retornam 0 há entre 1 e ele, se houver
# apenas 2 divisores então o número é primo, ainda são retornados os divisores do número, 
# primo ou não

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 52':^30}")
print('*' *30)

numero = int(input('Digite um número inteiro'))

divisoes = 0
divisores = []
for c in range (1, numero+1):
    if numero % c == 0:
        divisoes = divisoes + 1
        divisores.append(c)
        
if divisoes == 2:
    print(f'O número {numero} possui 2 divisões, é divisível por 1 e por ele mesmo, logo é um número primo')
elif divisoes > 2:
    print(f'O número {numero} possui {divisoes} divisões, é divisível por {divisores}, não sendo primo')
    
print('FIM')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)