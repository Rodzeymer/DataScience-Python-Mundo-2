numero = int(input('Digite um número inteiro'))

divisoes = 0
divisores = []
for c in range (1, numero+1):
    if numero % c == 0:
        divisoes = divisoes + 1
        divisores.append(c)
        
if divisoes == 2:
    print('O número {} possui 2 divisões, é divisível por 1 e por ele mesmo, logo é um número primo'.format(numero))
elif divisoes > 2:
    print('O número {} possui {} divisões, é divisível por {}, não sendo primo'.format(numero, divisoes, divisores))