nome = input('Digite o nome do aluno')
nota1 = float(input('Digite a primeira nota de {}'.format(nome)))
nota2 = float(input('Digite agora a segunda nota de {}'.format(nome)))

media = (nota1+nota2)/2

if media >=7:
    print('O aluno {} obteve media {:.2f}, estando portanto APROVADO!'.format(nome, media))
elif media < 7 and media >=5:
    print('O aluno {} atingiu a nota de {:.2f}, por isso está de RECUPERAÇÂO!'.format(nome, media))
elif media < 5:
    print('O aluno {} conseguiu atingir apenas a nota {:.2f} e está REPROVADO!'.format(nome, media))