# Agora inicamos o estudo de vetores para depois irmos para arrays, aqui o algoritmo pega os números pares
# entre 1 e 50, exibe na tela uma mensagem dizendo se o número é par e o acrescenta no vetor, exibindo o 
# o vetor completo ao final da execução

print('*' *30)
print("{'Python Mundo 2 - Desafio 47':^30}")
print('*' *30)

pares = []
for c in range (1, 50 ):
    if c %2 ==0:
        print(f'O número {c} é par')
        pares.append(c)
print(f'Os números pares entre 1 e 50 são {pares}')
        
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)