# Entrando no ramo de calculadoras, uma função muito interessante é a de fatoração, aqui o 
# desafio foi simples, criar um algoritmo que pegue o número e retorne o valor da fatoração
# desse número, exemplo o fatorial de e é 3x2x1 = 6, logo !3 é igual a 6, se fosse !10 ficaria
# 10x9x8x7x6x5x4x3x2x1, que retornaria o valor de 3.625.800. O programa pega o número e faz
# um loop dele, fazendo a multiplicação n vezes, sendo n o número informado, além disso foi
# demonstrado como fazer o cálculo utilizando o laço de repetição while e o laço for

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 60' :^30}")
print('*' *30)

fatorar1 = int(input('Digite um número para fatorar'))
fatorar2 = fatorar1
resultado1 = resultado2 = 1

while fatorar1 >=1:
    resultado1 = resultado1 * fatorar1
    fatorar1=fatorar1-1

for c in range(1, fatorar2):
    resultado2 = resultado2 * fatorar2
    fatorar2 = fatorar2-1
    
print(f'Resultado da fatoração com while = {resultado1}')
print(f'Resultado da fatoração com for = {resultado2}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)