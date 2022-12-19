altura = float(input('Digite a sua altura, em metros'))
peso = float(input('Agora digite o seu peso, em quilos'))

imc  = peso/(altura**2)
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

print('Com altura de {} metros e peso de {}kg, seu IMC é {:.2f} estando classificado como: {}'.format(altura, peso, imc, classeImc))