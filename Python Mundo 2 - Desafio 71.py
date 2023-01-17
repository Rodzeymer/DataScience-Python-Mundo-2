# Para encerrar esse Mundo 2 o boss se apresenta na forma de um algoritmo que simula
# um caixa eletrônico, em que o usuário solicita o saque de um valor inteiro qualquer e 
# o sistema responde quantas notas de 50, 20, 10, e 1 real serão dadas ao cliente.

# Para isso o sistema pega o valor total e testa quantas divisões inteiras são necessárias
# para reduzir o valor restante abaixo do valor de dada nota, de forma decrescente, em que
# para reduzir o valor do pedido para abaixo de 50 reais, por exemplo, quantas notas, divisões, 
# de 50 são necessárias, e passa o saldo restante do pedido para o teste do valor seguinte e 
# exibe na tela quantas notas foram dadas daquele valor, até que o saldo restante do pedido 
# seja menor que 10 qu é a quantidade de notas de 1 que serão dadas

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 71' :^30}")
print('*' *30)

saldoInicial = int(input('Quanto deseja sacar?'))
saldo = saldoInicial

print('Total de notas: ')
saque50 = saldo//50
saldo = saldo - (saque50*50)
if saque50>0:
    print(f'Notas de R$50: {saque50}')
saque20 = saldo//20
saldo = saldo - (saque20*20)
if saque20>0:
    print(f'Notas de R$20: {saque20}')
saque10 = saldo//10
saldo = saldo - (saque10*10)
if saque10>0:
    print(f'Notas de R10: {saque10}')
saque1 = saldo
if saque1>0:
    print(f'Notas de R$1: {saque1}')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)