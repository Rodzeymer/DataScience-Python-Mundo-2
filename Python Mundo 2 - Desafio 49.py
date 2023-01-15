# Uma rápida tabuada usando estrutura de repetição, fica um código bem enxuto e funcional, funciona com
# números decimais também

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 49':^30}")
print('*' *30)

tabuada = float(input('Digite um número para a tabuada'))
for c in range (1,11):
    resultado = tabuada*c
    print(f'{tabuada} x {c} = {resultado :.2f}')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)