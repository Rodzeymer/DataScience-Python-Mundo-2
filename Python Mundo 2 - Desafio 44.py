preco = float(input('Digite o valor do produto'))

print('O preço do produto é R${}, selecione o método de pagamento'.format(preco))
metodo = int(input('''
1 - para à vista, boleto ou PIX, com desconto de 10%;
2 - para à vista, no crédito ou débito, com desconto de 5%;
3 - para dividir em 2x no cartão, sem juros;
4 - para dividir em 3x ou mais no cartão, com juros de 20%'''))

if metodo == 1:
    valor = preco-preco*0.1
    print('À vista, boleto ou PIX, o valor final do produto fica por R${:.2f}, já com o desconto aplicado'.format(valor))
elif metodo == 2:
    valor = preco-preco*0.05
    print('À vista, no crédito ou débito, o valor final do produto fica por R${:.2f}, já com o desconto aplicado'.format(valor))
elif metodo == 3:
    valor = preco
    parcela = valor/2
    print('Dividindo sua compra em 2x no cartão de crédito, resulta em 2 parcelas de R${:.2f}, resultando no total de R${:.2f}'.format(parcela, valor))
elif metodo == 4:
    valor = preco+preco*0.2
    numParcelas = int(input('Digite em quantas parcelas quer dividir o valor de R${:.2f}'.format(valor)))
    parcela = valor / numParcelas
    print('Dividindo a compra de R${:.2f} em {} parcelas, com juros de 20%, resulta em compra final de R${:.2f}, com {} parcelas de R${:.2f}'
    .format(preco, numParcelas, valor, numParcelas, parcela))
else:
    print('Opção inválida')
    
print('Obrigado pela preferência!')