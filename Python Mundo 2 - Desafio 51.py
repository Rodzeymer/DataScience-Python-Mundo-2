primeiroTermo = float(input('Digite o primeiro termo da progressão'))
razao = float(input('Agora digite o valor da razão'))
termo = 10
for c in range(1, 11):
    progrssao = primeiroTermo*(c*razao)
    print('Na progressão, o termo {}, com razão {} é igual à {}'.format(c, razao, progrssao))