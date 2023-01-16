# Neste desafio vamos revisitar o algoritmo que calcula os 10 primeiros termos de uma 
# progressão aritmética, no desafio 51 foi usada a estrutura de repetição for, neste
# desafio vamos repetir mas usando a estrutura while para isso

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 61' :^30}")
print('*' *30)

primeiroTermo = int(input('Digite o primeiro termo da progressão'))
razao = int(input('Agora digite o valor da razão'))
termo = 10
decimoTermo = primeiroTermo + (10-1)* razao
print(f'''Progressão aritmética
    Primeiro termo {primeiroTermo}
    Razão {razao}''')
contador = 0
while contador <termo:
    progressao = primeiroTermo+(razao*contador)
    contador = contador +1
    print(f'{progressao} ', end='-> ')
print('FIM')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)