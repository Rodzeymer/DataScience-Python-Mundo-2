# Seguindo em calculadoras clássicas, vamos para a calculadora de IMC, neste programa o usuário informa
# a sua altura em centimetros e seu peso em metros, então o sistema calcula o seu IMC e responde com a 
# categoria, entre abaixo do peso, ideal, sobrepeso e obeso.

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 43':^30}")
print('*' *30) 

altura = float(input('Digite a sua altura, em centimetros'))
peso = float(input('Agora digite o seu peso, em quilos'))

imc  = peso/((altura/100)**2)
if imc< 18.5:
    classeImc = ('Abaixo do peso')
elif imc >=18.5 and imc <25:
    classeImc = ('Peso ideal')
elif imc >=25 and imc<30:
    classeImc = ('Sobrepeso')
elif imc>=30 and imc<40:
    classeImc = ('Obesidade')
elif imc>40:
    classeImc = ('Obesidade Mórbida')

print(f'Com altura de {(altura/100)} metros e peso de {peso}kg, seu IMC é {imc :.2f} estando classificado como: {classeImc}')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)