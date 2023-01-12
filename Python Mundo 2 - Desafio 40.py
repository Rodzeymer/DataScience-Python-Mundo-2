# Mais uma calculadora de médias, só pra usar f-strings e mostrar que o código fica mais limpo
# legível e menor

print('*' *30)
print("{'Python Mundo 2 - Desafio 40':^30}")
print('*' *30)
nome = input('Digite o nome do aluno')
nota1 = float(input(f'Digite a primeira nota de {nome}')
nota2 = float(input(f'Digite agora a segunda nota de {nome}')

media = (nota1+nota2)/2

if media >=7:
    print(f'O aluno {nome} obteve media {media :.2f}, estando portanto APROVADO!')
elif media < 7 and media >=5:
    print(f'O aluno {nome} atingiu a nota de {media :.2f}, por isso está de RECUPERAÇÂO!')
elif media < 5:
    print(f'O aluno {nome} conseguiu atingir apenas a nota {media :.2f} e está REPROVADO!')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)