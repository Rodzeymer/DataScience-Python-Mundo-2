continuar = 'S'

while continuar =='S':
    nome = str(input('Digite o nome da pessoa'))
    idade = int(input(f'Digite a idade de {nome}'))
    sexo = str(input(f'Digite o sexo de {nome}, [M/F]')).upper()
    