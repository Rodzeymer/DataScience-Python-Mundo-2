# Neste desafio foi construído um programa que entra num looping, solicitando um valor para se
# calcular a tabuada, enquanto o usuário não inserir a condição de parada, que é um valor 
# negativo o algoritmo segue rodando em looping

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 67' :^30}")
print('*' *30)

valorTabuada = 1

while valorTabuada>0:
    valorTabuada = int(input('Digite um valor para tabuada, ou um número negativo para interromper'))
    if valorTabuada <0:
        break
    for c in range(1,11):
        print(f'{valorTabuada} x {c} = {c*valorTabuada}')
print('FIM')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)