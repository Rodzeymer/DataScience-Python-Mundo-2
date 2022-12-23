valorTabuada = 1

while valorTabuada>0:
    valorTabuada = int(input('Digite um valor para tabuada, ou um número negativo para interromper'))
    if valorTabuada <0:
        break
    for c in range(1,11):
        print(f'{valorTabuada} x {c} = {c*valorTabuada}')
print('FIM')