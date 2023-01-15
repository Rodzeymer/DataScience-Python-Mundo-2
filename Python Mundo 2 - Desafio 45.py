# Neste desafio foi construido um algoritmo em que o usuário joga jokenpo, ou pedra, papel ou tesoura, 
# contra o computador. O usuário faz sua escolha, 1-Pedra, 2-Papel ou 3-Tesoura, o sistema escolhe usando
# o a função choice do módulo random de um array com as mesmas opções, o programa compara e exibe o resultado
# entre vitória do jogador, vitória do PC ou empate.

print('*' *30)
print("{'Python Mundo 2 - Desafio 45':^30}")
print('*' *30)

from random import choice

escolhaJogador = int(input('''Escolha entre:
1-Pedra;
2-Papel;
3-Tesoura'''))

if escolhaJogador>0 and escolhaJogador<4:
    escolhas = ['Pedra', 'Papel', 'Tesoura']
    escolhaJogador = escolhas[escolhaJogador-1]
    escolhaPC = choice(escolhas)

    if escolhaJogador == escolhaPC:
        print(f'EMPATE, o Jogador escolheu {escolhaJogador} e o PC escolheu {escolhaPC}')
        
    elif escolhaJogador == 'Pedra':
        if escolhaPC =='Papel':
            print(f'PC ganhou, Jogador escolhe {escolhaJogador} e PC escolheu {escolhaPC}')
        elif escolhaPC =='Tesoura':
            print(f'Jogador ganhou, Jogador escolhe {escolhaJogador} e PC escolheu {escolhaPC}')
   
    elif escolhaJogador == 'Papel':
        if escolhaPC =='Tesoura':
            print(f'PC ganhou, Jogador escolhe {escolhaJogador} e PC escolheu {escolhaPC}')
        
        elif escolhaPC =='Pedra':
            print(f'Jogador ganhou, Jogador escolhe {escolhaJogador} e PC escolheu {escolhaPC}')
    
    elif escolhaJogador == 'Tesoura':
        if escolhaPC =='Pedra':
            print(f'PC ganhou, Jogador escolhe {escolhaJogador} e PC escolheu {escolhaPC}')
        
        elif escolhaPC =='Papel':
            print(f'Jogador ganhou, Jogador escolhe {escolhaJogador} e PC escolheu {escolhaPC}')
else:
    print('Opção inválida')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)