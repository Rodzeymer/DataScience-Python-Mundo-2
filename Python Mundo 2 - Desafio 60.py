fatorar1 = int(input('Digite um número para fatorar'))
fatorar2 = fatorar1
resultado1 = resultado2 = 1


while fatorar1 >=1:
    resultado1 = resultado1 * fatorar1
    fatorar1=fatorar1-1

for c in range(1, fatorar2):
    resultado2 = resultado2 * fatorar2
    fatorar2 = fatorar2-1
    
print('Resultado da fatoração com while = {}'.format(resultado1))
print('Resultado da fatoração com for = {}'.format(resultado2))

