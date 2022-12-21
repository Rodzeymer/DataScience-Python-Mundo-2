pesos = []
for contador in range(1,6):
    peso = float(input('Digite o peso da pessoa {}'.format(contador)))
    pesos.append(peso)
    
pesosOrdenados = sorted(pesos)

maiorPeso = pesosOrdenados[len(pesosOrdenados)-1]
menorPeso = pesosOrdenados[0]
print(maiorPeso)
print(menorPeso)