# Para demosntrar que podemos aninhar, isso é colocar, if dentro de if, indefinidamente, inclusive dentro
# de outras estruturas condicionais e de laços de repetição esse algoritmo pega os números de 0 a 500 e
# testa para ver quais são ímpares e múltiplos de 3, simultâneamente, e realiza a soma desses, cujo valor 
# deverá ser de 20667

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 48':^30}")
print('*' *30)

soma = int(0)
for c in range (0, 500):
    if c%2!=0:
        if c %3 ==0:
            print(f'Número {c} é ímpar e múltiplo de 3')
            soma = soma+c
            
print(f'A soma de todos os números ímpares e múltiplos de 3 entre 1 e 500 é: {soma}')
        
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)