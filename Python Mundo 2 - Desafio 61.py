primeiroTermo = int(input('Digite o primeiro termo da progressão'))
razao = int(input('Agora digite o valor da razão'))
termos = int(input('Digite quantos termos deseja calcular'))-1
maisTermos = 1
while maisTermos !=0:
    termos = termos+maisTermos
    print('''Progressão aritmética
        Primeiro termo {}
        Razão {}
        Termos {}'''.format(primeiroTermo, razao, termos))
    contador = 0
    while contador <termos:
        progressao = primeiroTermo+(razao*contador)
        contador = contador +1
        print('{} '.format(progressao), end='-> ')
    print('FIM')
    maisTermos = int(input('Quer calcular mais termo?'))
print('Aplicativo encerrado!')