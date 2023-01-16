# Neste desafio fiz uma calculadora com repetição, ao final da operação ela pergunta se o 
# usuário deseja realizar outra operação, então o usuário informa o primeiro e o segundo valor
# e em seguida a operação desejada, o sistem retorna a operação com o seu resultado e pergunta
# se o usuário deseja realizar outra operação, o loop se repete até o digitar informar que não
# deseja continuar.

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 59' :^30}")
print('*' *30)

continuar = 'S'
while continuar == 'S':
    primeiroValor = float(input('Digite o primeiro valor'))
    segundoValor = float(input('Digite o segundo valor'))
    operacao = int(input(f'''Agora escolha qual operação executar entre {primeiroValor} e {segundoValor}
1 - Adição;
2 - Subtração;
3 - Multiplicação;
4 - Divisão'''))
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
    print(f'A operação resultande é {primeiroValor} {operador} {segundoValor} = {resultado}')
    continuar = str(input('Quer continuar? [S/N]')).upper()
print('Aplicativo encerrado, obrigado pela preferência!')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)