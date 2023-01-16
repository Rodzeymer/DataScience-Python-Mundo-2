# O desafio agora é fazer um jogo de par ou ímpar contra com computador, o susário escolhe
# entre par ou ímpar e o palpite, o algortimo escolhe um número, como só tem duas
# possibilidades, o programa passa por um if aninhado, que caso o usuário tenha escolhido par
# a condição de vitória é uma e caso seja ímpar é outra. Nesse programa a condição de parada 
# break é acionada quando o usuário perde e cada vitória é somada e uma mensagem informando
# o número de vitórias é exbibida

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 68' :^30}")
print('*' *30)

from random import randint

ganhou = True
vitorias = 0

while ganhou == True:
    aposta = input('Escolha, par ou impar? [P/I]').upper()
    escolha = int(input('Faça sua aposta, de 0 a 10'))
    
    if aposta == 'P':
        apostaExtenso = 'PAR'
        contraAposta = 'I'
    elif aposta =='I':
        apostaExtenso = 'ÍMPAR'
        contraAposta = 'P'
    else:
        print('Aposta inválida')
        break
    if escolha > 10 or escolha < 0:
        print('Número inválido')
        break
    contraEscolha = randint(0,10)
    
    resultado = escolha + contraEscolha
    print(f'Você escolheu {apostaExtenso}')
    print(f'O resultado foi {resultado}, você pediu {escolha} e o PC pediu {contraEscolha}')
    
    if resultado %2 == 0:
        ganhador = 'P'
    else:
        ganhador ='I'
    
    if aposta == ganhador:
        ganhou = True
        vitorias = vitorias +1
        print('PARABÉNS, VOCÊ GANHOU!')
    else:
        ganhou = False
        print('Infelizmente você perdeu')
        break
print(f'Você conseguiu vencer {vitorias} vezes seguidas')
print('Fim das apostas')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)