termos = int(input('Quantos termos de Fibonacci você quer calcular?'))
contador=1
fibonacci=[]
fibonacci.append(0)
fibonacci.append(1)

while contador < termos:
    novoFibonacci = fibonacci[contador]+fibonacci[contador-1]
    fibonacci.append(novoFibonacci)
    contador=contador+1
print('Os primeiros {} termos da sequencia de Fibonacci são:'.format(termos))
print(fibonacci)