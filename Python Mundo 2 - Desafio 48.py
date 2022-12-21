soma = int(0)
for c in range (0, 500):
    if c%2!=0:
        if c %3 ==0:
            print('Número {} é ímpar e múltiplo de 3'.format(c))
            soma = soma+c
            
print(soma)