soma=0
for c in range(0,6):
    numero = int(input('Digite um número inteiro'))
    if numero %2 == 0:
        soma=soma+numero
print('A soma dos números inteiros é: {}'.format(soma))