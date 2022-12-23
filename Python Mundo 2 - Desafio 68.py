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