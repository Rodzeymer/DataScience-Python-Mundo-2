primeiroTermo = int(input('Digite o primeiro termo da progressão'))
razao = int(input('Agora digite o valor da razão'))
termo = 10
decimoTermo = primeiroTermo + (10-1)* razao
print('''Progressão aritmética
    Primeiro termo {}
    Razão {}'''.format(primeiroTermo, razao))
contador = 0
while contador <termo:
    progressao = primeiroTermo+(razao*contador)
    contador = contador +1
    print('{} '.format(progressao), end='-> ')
print('FIM')