# Só pra dar uma desacelerada, construir um algoritmo que pede para o usuário digitar 6 números inteiros,
# identifica e soma os pares desconsiderando os ímpares, com estrutura de repetição a escrita fica mais 
# ágil

print('*' *30)
print("{'Python Mundo 2 - Desafio 50':^30}")
print('*' *30)

soma=0
for c in range(0,6):
    numero = int(input('Digite um número inteiro'))
    if numero %2 == 0:
        soma=soma+numero
print(f'A soma dos números inteiros é: {soma}')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)