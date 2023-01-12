# Então, falando em clássicos, a calculadora de alistamento, o programa que lê a idade 
# e o sexo de uma pessoa e calcula se está na época de se alistar para o exercício militar, 
# ou quanto tempo falta ou se passou do prazo, enviando uma mensagem para cada uma dos 6 casos
# de retorno.

print('*' *30)
print("{'Python Mundo 2 - Desafio 39':^30}")
print('*' *30)
genero = input('Digite o seu genero, M para Masculino, F para feminino').lower()
idade = int(input('Digite a sua idade'))

if genero == 'm':
    if idade < 18:
        print(f'Ainda não está na época de se alistar, faltam {18-idade} anos para isso')
    elif idade > 18:
        print(f'Já passou da época do alistamento, vocês está {idade-18} anos atrasado')
    else:
        print('Está na época do seu alistamento militar procure o quartel da sua região e se informe sobre o seu dever cívico-militar')
elif genero =='f':
    if idade <18:
        print(f'Ainda não chegou a época de se decidir pelo alistamento, faltam {18-idade} anos para isso')
    elif idade > 18:
        print(f'Passou {idade-18} anos do alistamento militar voluntário')
    else:
        print('Esse é o ano em que você pode decidir se alistar ou não, parabéns!')
else:
    print('Opção inválida, tente novamente')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)