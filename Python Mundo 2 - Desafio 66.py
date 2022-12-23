numeroNovo = int(0)
numeros = []
soma=0

while numeroNovo != 999:
    numeroNovo = int(input('Digite um número qualquer ou digite 999 para encerrar'))
    if numeroNovo==999:
        break
    numeros.append(numeroNovo)
    soma=soma+numeroNovo
quantosNumeros = len(numeros)

print('Foram digitados {} números'.format(quantosNumeros))
print('A soma desses números é: {}'.format(soma))