# Avançando um degrau na complexidade de calculadoras, temos essa que foi construída para calcular, dado
# o valor do produto, o preço final conforme o método de pagamento escolhido, o usuário insere o valor e 
# o sistema oferece 4 métodos de pagamento, à vista, pix ou dividir no cartão, cada qual com seu desconto
# ou juros, exibindo ao final qual foi o método, valor original e final do produto e, se parcelado, quantas
# parcelas e seus valores.

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 44':^30}")
print('*' *30)

preco = float(input('Digite o valor do produto'))

print(f'O preço do produto é R${preco}, selecione o método de pagamento')
metodo = int(input('''
1 - para à vista, boleto ou PIX, com desconto de 10%;
2 - para à vista, no crédito ou débito, com desconto de 5%;
3 - para dividir em 2x no cartão, sem juros;
4 - para dividir em 3x ou mais no cartão, com juros de 20%'''))

if metodo == 1:
    valor = preco-preco*0.1
    print(f'À vista, boleto ou PIX, o produto vendido por {preco} fica com o valor final de R${valor :.2f}, com o desconto aplicado')
elif metodo == 2:
    valor = preco-preco*0.05
    print(f'À vista, no crédito ou débito, o valor final do produto fica por R${valor :.2f}, já com o desconto de R${preco-valor} aplicado')
elif metodo == 3:
    valor = preco
    parcela = valor/2
    print(f'Dividindo sua compra em 2x no cartão de crédito, resulta em 2 parcelas de R${parcela :.2f}, resultando no total de R${valor :.2f}')
elif metodo == 4:
    valor = preco+preco*0.2
    numParcelas = int(input(f'Digite em quantas parcelas quer dividir o valor de R${valor :.2f}'))
    parcela = valor / numParcelas
    print(f'Dividindo a compra de R${preco :.2f} em {numParcelas} parcelas, com juros de 20%, resulta em compra final de R${valor:.2f}, com {numParcelas} parcelas de R${parcela:.2f}')
else:
    print('Opção inválida')
    
print('Obrigado pela preferência!')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)