# Para encerrar esse Mundo 2 o boss se apresenta na forma de um algoritmo que simula
# um caixa eletrônico

# <><><><><><>< TERMINAR DE COMENTAR O QUANTO ANTES <><><><><><><

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