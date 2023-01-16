# Mais um desafio com condição de parada, enquanto o usuário digitar s para sim continuar a 
# execução do programa, ele vai lendo os números digitados por ele e ao final, quando ele 
# digitar algo diferente de s o programa se encerra, apresentando as mensagens de quantos
# números foram digitados, o maior e o menor, pois o algoritmo vai alimentando um vetor com os
# números inseridos e comparando o maior e o menor, até a condição de parada for aplicada

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 65' :^30}")
print('*' *30)

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

print(f'A média dos números digitados foi {media}')
print(f'O maior número digitado foi {numeroMaior}')
print(f'O menor número digitado foi {numeroMenor}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)