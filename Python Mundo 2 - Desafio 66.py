# Voltando ao desafio 64, a condição de parada continua sendo o usuário digitar 999, mas
# dessa vez há a instrução break, que interrompe o a execução do laço de repetição, impedindo
# assim que as instruções restantes do laço sejam executadas, como você pode ver, se não fosse
# pela instrução break o 999 seria adicionado à contagem de números e à soma, o que ocorre no 
# desafio 64

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 66' :^30}")
print('*' *30)

numeroNovo = int(0)
numeros = []
soma=0

while numeroNovo != 999:
    numeroNovo = int(input('Digite um número qualquer ou digite 999 para encerrar'))
    if numeroNovo==999:
        break
    numeros.append(numeroNovo)
    soma=soma+numeroNovo
quantosNumeros = len(numeros)

print(f'Foram digitados {quantosNumeros} números')
print(f'A soma desses números é: {soma}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)