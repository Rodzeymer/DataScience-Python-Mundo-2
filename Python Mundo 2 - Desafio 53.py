frase = str(input('Digite uma frase')).lower()

fraseSemEspacos = frase.replace(' ', '')

fraseOposta = fraseSemEspacos[::-1]

if fraseSemEspacos == fraseOposta:
    print('{} é um palindromo ficando {} quando invertida'.format(frase, fraseOposta))
else:
    print('{} não é um palíndromo, ficando {} quando invertida'.format(frase, fraseOposta))
