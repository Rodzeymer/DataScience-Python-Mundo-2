continuar = 'S'
menorPreco = float(0)
produtos = 0
produtosArray =[]
soma = 0
produtosMaisMil = 0
while continuar !='N':
    produtoNome = input('Digite o nome do produto')
    preco = float(input(f'Digite o valor de {produtoNome}'))
    if len(produtosArray) == 0:
        menorNome = produtoNome
        menorPreco = preco
    if preco < menorPreco:
        menorPreco = preco
        menorNome = produtoNome
    produtos = produtos+1
    if preco > 1000:
        produtosMaisMil = produtosMaisMil+1
    soma = soma + preco
    produtosArray.append(produtoNome)
    continuar = input('Quer adicionar mais itens à lista? [S/N]').upper()

print(f'Quantidade de produtos da lista é {produtos}')
print(f'Menor preço encontrado foi do produto {menorNome} que custou R${menorPreco}')
print(f'Foram adicionados {produtosMaisMil} Produtos acima de mil reais')
print(f'Total da lista foi R${soma}')
    