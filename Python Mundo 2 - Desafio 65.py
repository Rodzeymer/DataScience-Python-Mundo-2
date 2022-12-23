continuar = 'S'
numerosDigitados = []
soma = 0

while continuar == 'S':
    numero = int(input('Digite um novo número'))
    soma = soma + numero
    if not numerosDigitados:
        numeroMaior = numero
        numeroMenor = numero
    numerosDigitados.append(numero)
    if numero > numeroMaior:
        numeroMaior = numero
    if numero < numeroMenor:
        numeroMenor = numero
    continuar = input('Deseja continuar?').upper()
media = soma/len(numerosDigitados)

print('A média dos números digitados foi {}'.format(media))
print('O maior número digitado foi {}'.format(numeroMaior))
print('O menor número digitado foi {}'.format(numeroMenor))
