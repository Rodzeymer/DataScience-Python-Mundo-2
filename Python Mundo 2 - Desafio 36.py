# Vamos de Mundo 2, já começando quente temos o algorito que calcula se o financiamento 
# de uma casa pode ser aprovada, tendo como base de cálculo a renda do comprador, o preço
# da casa e em quanto tempo o comprador pretende quitar esse financiamento.

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 36':^30}")
print('*' *30)
renda = float(input('Qual a renda do comprador?'))
precoCasa = float(input('Qual o valor da casa que quer comprar?'))
tempoFinanciamento = int(input('Deseja pagar a casa em quantos anos?'))
valorPrestacao = precoCasa / (tempoFinanciamento*12)


if valorPrestacao > renda*0.3:
	print(f'O financiamento ficaria em {tempoFinanciamento*12} vezes de R${valorPrestacao :.2f}, acima do recomendado para sua renda que é de R${renda*0.3 :.2f}, correspondendo a 30% dela.')
else: 
	print(f'O seu orçamento comporta a parcela de R${valorPrestacao :.2f} por {tempoFinanciamento*12} meses, pois fica abaixo dos 30% de seu orçamento, R${renda*0.3 :.2f}')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)