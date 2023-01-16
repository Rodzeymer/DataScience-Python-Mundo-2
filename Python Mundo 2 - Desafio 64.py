# Neste desafio um programa simples para demonstrar o que é uma condição de parada, condição
# de parada é aquela que interrompe o loop, jogando o fluxo de andamento do algoritmo pra fora
# da estrutura de repetição e completando o processamento do algoritmo. Para isso foi criado
# esse programa que pede para o usuário digitar um número qualquer, enquanto o usuário não 
# digitar 999 o algoritmo continua a trabalhar na execução, quando for digitado 999 o programa
# interrompe a repetição com uma resposta informando quantos números foram digitados e qual a
# soma dos números digitados antes de se encerrar o loop

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 64' :^30}")
print('*' *30)
numeroNovo = int(0)
numeros = []
soma=0
c=0
numeroNovo = int(input('Digite um número qualquer ou digite 999 para encerrar'))
while numeroNovo != 999:
    numeros.append(numeroNovo)
    soma=soma+numeroNovo
    numeroNovo = int(input('Digite um número qualquer ou digite 999 para encerrar'))
quantosNumeros = len(numeros)

print(f'Foram digitados {quantosNumeros} números')
print(f'A soma desses números é: {soma}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)