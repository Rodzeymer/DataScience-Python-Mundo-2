nomes = []
idades = []
sexos = []
somaIdades = 0
mulherMenor =0
    
for contador in range (1,5):
    print('<<{}ª Pessoa>>'.format(contador))
    nome = str(input('Digite o nome da pessoa {}'.format(contador))).strip()
    nomes.append(nome)
    idade = int(input('Digite a idade de {}'.format(nome)))
    idades.append(idade)
    somaIdades = somaIdades+idade
    sexo = str(input('Digite o sexo de {}, [M/F]'.format(nome))).strip()
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
print('A média das idades dos 4 integrantes é {}'.format(mediaIdades))
print('O homem mais velho é {}, com a idade de {} anos'.format(nomeMaisVelho, maiorIdade))
print('O grupo possui {} mulheres com menos de 20 anos'.format(mulherMenor))