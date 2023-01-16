# Agora iremos manipular uma string e identificar se o que o usuário digitou é um palindromo, 
# conceito em que uma palavra ou frase pode ser lida da mesma forma de trás pra frente,
# desconsiderando-se espaços e acentuações, para isso removemos todos os espaços e invertemos
# a string, armazenando-a em outra variável, se a original e a reversa forem iguais então
#temos um palindromo

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 53':^30}")
print('*' *30)

frase = str(input('Digite uma frase')).lower()

fraseSemEspacos = frase.replace(' ', '')
fraseOposta = fraseSemEspacos[::-1]

if fraseSemEspacos == fraseOposta:
    print(f'{frase} é um palindromo ficando {fraseOposta} quando invertida')
else:
    print(f'{frase} não é um palíndromo, ficando {fraseOposta} quando invertida')

print('FIM')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)