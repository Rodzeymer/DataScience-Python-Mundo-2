numeroNovo = int(0)
numeros = []
soma=0
c=0

while numeroNovo != 999:
    numeroNovo = int(input('Digite um número qualquer ou digite 999 para encerrar'))
    numeros.append(numeroNovo)
    soma=soma+numeroNovo
numerosCerto = numeros.pop()
quantosNumeros = len(numeros)
soma = soma-999

print('Foram digitados {} números'.format(quantosNumeros))
print('A soma desses números é: {}'.format(soma))