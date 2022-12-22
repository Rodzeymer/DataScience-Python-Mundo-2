sexo = 'k'

while sexo not in 'MF':
    sexo = str(input('Digite o seu sexo [M/F]')).upper()
    if sexo in 'MF':
        print('Sexo {} é válido'.format(sexo))
    else:
        print('Sexo {} não é válido'.format(sexo))
