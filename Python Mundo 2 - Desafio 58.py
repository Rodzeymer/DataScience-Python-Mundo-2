# Seguindo a linha de algoritmos que se repetem até o usuário atingir determinada condição ou
# dar a entrada correta, aqui temos mais um desafio que foi o de fazer mais um jogo de
# adivinhação aqui o usuário tenta adivinhar qual número o sistema escolhe, de 1 a 10, se o 
# usuário errar ele pode tentar até acertar, quando acertar o algoritmo retorna quantas
# tentativas foram necesárias para acertar

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 58':^30}")
print('*' *30)

from random import randint

palpite=int(input('Tente adivinhar o número da sorte, de 1 a 10'))
palpites = 1
numeroSorte = randint(1, 10)
while palpite != numeroSorte:
    palpites = palpites+1
    print(f'Você chutou {palpite}, mas errou, tente novamente')
    palpite=int(input('Tente adivinha o número da sorte, de 1 a 10'))
print(f'ACERTOU, o número sorteado foi {palpite}, foram {palpites} palpites até acertar')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)