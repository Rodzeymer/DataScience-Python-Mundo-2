genero = input('Digite o seu genero, M para Masculino, F para feminino').lower()

idade = int(input('Digite a sua idade'))

if genero == 'm':
    if idade < 18:
        print('Ainda não está na época de se alistar, faltam {} anos para isso'.format(18-idade))
    elif idade > 18:
        print('Já passou da época do alistamento, vocês está {} anos atrasado'.format(idade-18))
    else:
        print('Está na época do seu alistamento militar procure o quartel da sua região e se informe sobre o seu dever cívico-militar')
elif genero =='f':
    if idade <18:
        print('Ainda não chegou a época de se decidir pelo alistamento, faltam {} anos para isso'.format(18-idade))
    elif idade > 18:
        print('Passou {} anos do alistamento militar voluntário'.format(idade-18))
    else:
        print('Esse é o ano em que você pode decidir se alistar ou não, parabéns!')
else:
    print('Opção inválida, tente novamente')