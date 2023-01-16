# Agora a calculadora da Progressão aritmética irá solicitar ao usuário quantos termos ele 
# deve calcular e ao final do cálculo repetir a pergunta e incluir na quantidade de termos a 
# serem calculados e ir incremetando até que o usuário decida encerrar, para isso aninhamos
# duas estruturas while, a primeira garante que o usuário quer mais termos e a segunda adiciona
# essa quantidade de termos a mais na repetição, realizando o cálculo devido e informando o 
# usuário dos termos, do começo ao fim

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 62' :^30}")
print('*' *30)

primeiroTermo = int(input('Digite o primeiro termo da progressão'))
razao = int(input('Agora digite o valor da razão'))
termos = int(input('Digite quantos termos deseja calcular'))-1
maisTermos = 1
while maisTermos > 0:
    termos = termos+maisTermos
    print(f'''Progressão aritmética
        Primeiro termo {primeiroTermo}
        Razão {razao}
        Termos {termos}''')
    contador = 0
    while contador <termos:
        progressao = primeiroTermo+(razao*contador)
        contador = contador +1
        print(f'{progressao} ', end='-> ')
    print('FIM')
    maisTermos = int(input('Quer calcular quantos termos a mais? 0 encerra a aplicação'))
print('Aplicativo encerrado!')

print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)