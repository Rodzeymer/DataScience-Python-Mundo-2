soma = int(0)
for c in range (0, 500):
    if c%2!=0:
        if c %3 ==0:
            print('Número {} é ímpar e múltiplo de 3'.format(c))
            soma = soma+c
            
print('A soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é: {}'.format(soma))