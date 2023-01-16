# Agora com a noção de condição de parada e familiarizado com a instrução break, vamos refazer
# o desafio em que o algoritmo lia o nome, idade e sexo das pessoas, mas agora quem define a 
# quantidade de pessoas inseridas no sistema é o usuário, que executa a inserção até que opte 
# por não continuar a execução do algoritmo, ao final será exibida a mensagem contabilizando 
# quantas pessoas foram inseridas, quantas mulheres acima de 20 anos, quantos homens e quantas
# pessoas acima de 18 anos. 

# Para isso o algoritmo entra em um loop solicitando as informações de cada pessoa e vai 
# alimentando os vetores à medida que os if vão sendo executados, assim há o processo de 
# de separação dos diferentes perfis e ocorre a exibição do seu resultado ao final

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 69' :^30}")
print('*' *30)

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

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)