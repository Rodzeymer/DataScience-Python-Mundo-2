# Com a progrssão comum feita, podemos aplicar o mesmo princípio para a sequencia Fibonacci, 
# progressão com primeiro termo e razão conhecidos, então basta o usuário determinar quantos
# termos serão calculados, a sequencia Fibonacci começa com 0 depois vai pra 1 e apartir de 
# então os proximos termos serão sempre a soma dos dois anteriores, então 0+1 = 1, 1+1 = 2, 
# 1+2 = 3, 2+3 = 5, 3+5 = 8 e assim indefinidamente

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 63' :^30}")
print('*' *30)
termos = int(input('Quantos termos de Fibonacci você quer calcular?'))
contador=1
fibonacci=[]
fibonacci.append(0)
fibonacci.append(1)

while contador < termos-1:
    novoFibonacci = fibonacci[contador]+fibonacci[contador-1]
    fibonacci.append(novoFibonacci)
    contador=contador+1
print(f'Os primeiros {termos} termos da sequencia de Fibonacci são:')
print(fibonacci)

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)