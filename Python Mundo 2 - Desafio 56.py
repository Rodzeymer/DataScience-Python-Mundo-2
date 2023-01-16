# Neste desafio o algoritmo deve, num grupo de 4 pessoas a serem informadas pelo usuário, 
# registrar a idade de todos, retornando a média; identificar o homem mais velho do grupo e 
# informar quantas mulheres tem menos de 20 anos. Para isso iremos colocar num loop de 4
# iterações os pedidos para o usuário informar os nomes, idades e sexo dos 4 integrantes, 
# em que vão ficar registrados, em vetores diferentes, os nomes, pesos e sexos, para então
# identificar o homem de maior idade, e realizar a soma das mulheres com mais de 20 anos e 
# ao final realizar a média de todas as idades informadas

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 56':^30}")
print('*' *30)

nomes = []
idades = []
sexos = []
somaIdades = 0
mulherMenor =0
    
for contador in range (1,5):
    print('<<{}ª Pessoa>>'.format(contador))
    nome = str(input(f'Digite o nome da pessoa {contador}')).strip()
    nomes.append(nome)
    idade = int(input(f'Digite a idade de {nome}'))
    idades.append(idade)
    somaIdades = somaIdades+idade
    sexo = str(input(f'Digite o sexo de {nome}, [M/F]')).strip()
    sexos.append(sexo)
    if sexo in'Mm' and contador == 1:
        maiorIdade = idade
        nomeMaisVelho = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeMaisVelho= nome
    if sexo in 'Ff' and idade <= 20:
        mulherMenor=+1

mediaIdades=somaIdades/len(idades)
print(f'A média das idades dos 4 integrantes é {mediaIdades}')
if sexo not in 'Mm':
    print('Neste grupo não há homens')
elif sexo in 'Mm':
    print(f'O homem mais velho é {nomeMaisVelho}, com a idade de {maiorIdade} anos')
print(f'O grupo possui {mulherMenor} mulheres com menos de 20 anos')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)