# Semelhante ao desafio passado, mas agora vamos classificar o peso, o usuário informa o peso
# de 5 pessoas e o sistema irá retornar, dentre eles, o maior e o menor peso, só que dessa 
# vez o código não apresenta "macetes" para funcionar de forma adequada

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 55':^30}")
print('*' *30)

pesos = []
for contador in range(1,6):
    peso = float(input(f'Digite o peso da pessoa {contador}'))
    pesos.append(peso)
    
pesosOrdenados = sorted(pesos)

maiorPeso = pesosOrdenados[len(pesosOrdenados)-1]
menorPeso = pesosOrdenados[0]

print(f'O maior peso registrado foi o de {maiorPeso}Kg')
print(f'O menor peso registrado foi o de {menorPeso}Kg')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)