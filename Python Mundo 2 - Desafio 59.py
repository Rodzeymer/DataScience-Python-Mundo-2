continuar = 'S'
while continuar == 'S':
    primeiroValor = float(input('Digite o primeiro valor'))
    segundoValor = float(input('Digite o segundo valor'))
    operacao = int(input('''Agora escolha qual operação executar entre {} e {}
1 - Adição;
2 - Subtração;
3 - Multiplicação;
4 - Divisão'''.format(primeiroValor, segundoValor)))
    if operacao == 1:
        resultado = primeiroValor+segundoValor
        operador = "+"
    elif operacao == 2:
        resultado = primeiroValor-segundoValor
        operador = "-"
    elif operacao == 3:
        resultado = primeiroValor*segundoValor
        operador = "*"
    elif operacao == 4:
        resultado = primeiroValor/segundoValor
        operador = "/"
    else:
        print('Operação inválida, escolha dentre as 4 operações básicas')
    print('A operação resultande é {} {} {} = {}'.format(primeiroValor, operador, segundoValor, resultado))
    continuar = str(input('Quer continuar? [S/N]')).upper()
print('Aplicativo encerrado, obrigado pela preferência!')