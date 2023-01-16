# Vamos ver uma calculadora que retorna os 10 primeiros termos de uma progressão aritmética 
# baseado no primeiro termo e no valor da razão informados pelo usuário 

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 51':^30}")
print('*' *30)

primeiroTermo = int(input('Digite o primeiro termo da progressão'))
razao = int(input('Agora digite o valor da razão'))
termo = 10
decimoTermo = primeiroTermo + (10-1)* razao
print(f'''Progressão aritmética
    Primeiro termo {primeiroTermo}
    Razão {razao}''')
for c in range(primeiroTermo, decimoTermo + razao, razao):
    print(f'{c} ', end='-> ')
    
print('FIM')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)