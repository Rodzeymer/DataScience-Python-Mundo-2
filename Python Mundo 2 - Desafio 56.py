nomes = []
idades = []
sexos = []
    
for contador in range (1,3):
    nome = str(input('Digite o nome da pessoa {}'.format(contador)))
    nomes.append(nome)
    idade = int(input('Digite a idade de {}'.format(nome)))
    idades.append(idade)
    sexo = str(input('Digite o sexo de {}'.format(nome)))
    sexos.append(sexo)

