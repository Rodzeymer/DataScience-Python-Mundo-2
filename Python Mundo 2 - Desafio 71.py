saldoInicial = int(input('Quanto deseja sacar?'))
saldo = saldoInicial

saque50 = saldo//50
saldo = saldo - (saque50*50)
saque20 = saldo//20
saldo = saldo - (saque20*20)
saque10 = saldo//10
saldo = saldo - (saque10*10)
saque1 = saldo

print(f'''Total de notas:
Notas de R$50: {saque50}
Notas de R$20: {saque20}
Notas de R$10: {saque10}
Notas de R$1: {saque1}


''')
