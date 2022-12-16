renda = float(input('Qual a renda do comprador?'))

precoCasa = float(input('Qual o valor da casa que quer comprar?'))

tempoFinanciamento = int(input('Deseja pagar a casa em quantos anos?'))

valorPrestacao = precoCasa / (tempoFinanciamento*12)

if valorPrestacao > renda*0.3:
	print('O financiamento ficaria em {} vezes de R${:.2f}, acima do recomendado para sua renda que é de R${:.2f}, correspondendo a 30% dela.'.format(tempoFinanciamento*12, valorPrestacao, renda*0.3))
else: 
	print('O seu orçamento comporta a parcela de R${:.2f} por {} meses, pois fica abaixo dos 30% de seu orçamento, R${:.2f}'.format(valorPrestacao, tempoFinanciamento*12, renda*0.3))