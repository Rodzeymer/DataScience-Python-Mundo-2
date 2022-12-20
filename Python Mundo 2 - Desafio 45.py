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
        print('EMPATE, o Jogador escolheu {} e o PC escolheu {}'.format(escolhaJogador, escolhaPC))

    elif escolhaJogador == 'Pedra':
        if escolhaPC =='Papel':
            print('PC ganhou, Jogador escolhe {} e PC escolheu {}'.format(escolhaJogador, escolhaPC))
        elif escolhaPC =='Tesoura':
            print('Jogador ganhou, Jogador escolhe {} e PC escolheu {}'.format(escolhaJogador, escolhaPC))

    elif escolhaJogador == 'Papel':
        if escolhaPC =='Tesoura':
            print('PC ganhou, Jogador escolhe {} e PC escolheu {}'.format(escolhaJogador, escolhaPC))
        elif escolhaPC =='Pedra':
            print('Jogador ganhou, Jogador escolhe {} e PC escolheu {}'.format(escolhaJogador, escolhaPC))

    elif escolhaJogador == 'Tesoura':
        if escolhaPC =='Pedra':
            print('PC ganhou, Jogador escolhe {} e PC escolheu {}'.format(escolhaJogador, escolhaPC))
        elif escolhaPC =='Papel':
            print('Jogador ganhou, Jogador escolhe {} e PC escolheu {}'.format(escolhaJogador, escolhaPC))

else:
    print('Opção inválida')