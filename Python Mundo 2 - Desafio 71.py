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