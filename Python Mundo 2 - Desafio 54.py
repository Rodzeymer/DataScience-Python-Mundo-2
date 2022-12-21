from datetime import date

anoAtual = date.today().year
maiorIdade = 0
menorIdade = 0
maiores =[]
menores = []
for contador in range(1,8):
    anoNascimento = int(input('Digite o ano de nascimento da pessoa {}'.format(contador)))
    idade = anoAtual-anoNascimento
    if idade >=18:
        maiorIdade = maiorIdade +1
        maiores.append(idade)
    else:
        menorIdade = menorIdade+1
        menores.append(idade)
print('Dentre as 7 pessoas, {} atingiram a maioridade e {} ainda são menor de idade'.format(maiorIdade, menorIdade))
print('As pessoas de maior idade possuem idades de {}'.format(maiores))
print('As pessoas de menor idade possuem idades de {}'.format(menores))