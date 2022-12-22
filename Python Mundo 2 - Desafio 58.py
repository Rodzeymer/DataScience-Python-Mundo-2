from random import randint

palpite=int(input('Tente adivinhar o número da sorte, de 1 a 10'))
palpites = 1
numeroSorte = randint(1, 10)
while palpite != numeroSorte:
    palpites = palpites+1
    print('Você chutou {}, mas errou, tente novamente'.format(palpite))
    palpite=int(input('Tente adivinha o número da sorte, de 1 a 10'))
print('ACERTOU, o número sorteado foi {}, foram {} palpites até acertar'.format(palpite, palpites))
