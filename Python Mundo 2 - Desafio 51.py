primeiroTermo = int(input('Digite o primeiro termo da progressão'))
razao = int(input('Agora digite o valor da razão'))
termo = 10
decimoTermo = primeiroTermo + (10-1)* razao
print('''Progressão aritmética
    Primeiro termo {}
    Razão {}'''.format(primeiroTermo, razao))
for c in range(primeiroTermo, decimoTermo + razao, razao):
    print('{} '.format(c), end='-> ')
print('FIM')