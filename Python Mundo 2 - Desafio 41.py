# Agora o programa irá pegar o ano de nascimento que o usuário informar e comparar com o ano
# atual do sistema, recuperado pelo próprio sistema através do módulo datetime, com base então na
# idade calculada o sistema irá apresentar ao usuário uma categoria etária

print('*' *30)
print("{'Python Mundo 2 - Desafio 41':^30}")
print('*' *30) 

from datetime import date
anoAtual = int(date.today().year)

anoNascimento = int(input('Digite o ano do seu nascimento'))
idade  = anoAtual  - anoNascimento

if idade <=9:
    print(f'Seja muito bem vindo, com a sua idade {idade} a sua categoria é Mirim')
elif idade>9 and idade <=14:
    print(f'Olá, por conta da sua idade ser {idade}, sua categoria é a Infantil')
elif idade>14 and idade <=19:
    print(f'Parabéns, com {idade} anos, sua categoria é Junior')
elif idade >19 and idade <=20:
    print(f'Com {idade} anos sua categoria é Sênior')
elif idade > 20 and idade <=80:
    print(f'Maravilha, com a idade de {idade} sua categoria é a mais alta, a categoria Master')
else:
    print(f'Nossos agradecimentos, com a idade de {idade} anos é um prazer ainda tê-lo conosco, na categora Master!')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)