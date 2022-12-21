tabuada = float(input('Digite um número para a tabuada'))

for c in range (1,11):
    resultado = tabuada*c
    print('{} x {} = {:.2f}'.format(tabuada, c, resultado))