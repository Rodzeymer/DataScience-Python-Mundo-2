# O desafio agora é receber o ano de nascimento de 7 pessoas, identificar quem tem mais de 
# 21 anos e identificar quanto possuem 21 anos ou mais, que são menores de idade e quais são
# as suas idades, depois de pegar o ano atual do sistema, fiz um loop pedindo a idade de 7 
# pessoas, passando por um if que verifica a idade e adiciona em um vetor os maiores de 21
# e em outro os menores e ao final exibe as mensagens de quantas pessoas possuem 21 anos ou mais
# e menores e as idades dos dois grupos

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 54':^30}")
print('*' *30)

from datetime import date

anoAtual = date.today().year
maiorIdade = 0
menorIdade = 0
maiores =[]
menores = []
for contador in range(1,8):
    anoNascimento = int(input(f'Digite o ano de nascimento da pessoa {contador}'))
    idade = anoAtual-anoNascimento
    if idade >=21:
        maiorIdade = maiorIdade +1
        maiores.append(idade)
    else:
        menorIdade = menorIdade+1
        menores.append(idade)
print(f'Dentre as 7 pessoas, {maiorIdade} atingiram a maioridade e {menorIdade} ainda são menor de idade')
print(f'As pessoas de maior idade possuem idades de {maiores}')
print(f'As pessoas de menor idade possuem idades de {menores}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)