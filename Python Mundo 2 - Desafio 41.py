from datetime import date

anoAtual = int(date.today().year)

anoNascimento = int(input('Digite o ano do seu nascimento'))
idade  = anoAtual  - anoNascimento

if idade <=9:
    print('Seja muito bem vindo, com a sua idade {} a sua categoria é Mirim'.format(idade))
elif idade>9 and idade <=14:
    print('Olá, por conta da sua idade ser {}, sua categoria é a Infantil'.format(idade))
elif idade>14 and idade <=19:
    print('Parabéns, com {} anos, sua categoria é Junior'.format(idade))
elif idade >19 and idade <=20:
    print('Com {} anos sua categoria é Sênior'.format(idade))
elif idade > 20 and idade <=80:
    print('Maravilha, com a idade de {} sua categoria é a mais alta, a categoria Master'.format(idade))
else:
    print('Nossos agradecimentos, com a idade de {} anos é um prazer ainda tê-lo conosco, na categora Master!'.format(idade))