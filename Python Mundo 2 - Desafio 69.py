continuar = 'S'
sexo = ''
maiorIdade=0
mulheresIdade=0
homens=0
pessoas=0
while continuar !='N':
    sexo=''
    nome = str(input('Digite o nome da pessoa'))
    idade = int(input(f'Digite a idade de {nome}'))
    while sexo !='M'and sexo !='F':
        sexo = str(input(f'Digite o sexo de {nome}, [M/F]')).upper()
    pessoas=pessoas+1
    if idade > 18:
        maiorIdade = maiorIdade +1
    if idade >= 20 and sexo=='F':
        mulheresIdade = mulheresIdade +1
    if sexo=='M':
        homens= homens+1
    continuar = input('Deseja continuar? [S/N]').upper()
print(f'Foram inseridas {pessoas} pessoas')
print(f'Foram cadastradas {mulheresIdade} mulheres com 20 anos ou mais')
print(f'Foram inseridos {homens} homens')
print(f'Foram inseridas {maiorIdade} pessoas maiores de 18 anos')