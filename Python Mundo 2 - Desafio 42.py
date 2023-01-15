# Seguindo o aumento da complexidade das calculadoras, agora o sistema irá perguntar as medidas dos 
# lados de um triângulo, e, em sendo possível a construção desse triângulo irá determinar que tipo de 
# triângulo ele é: isóceles, equilátero, ou escaleno.

print('*' *30)
print(f"{'Python Mundo 2 - Desafio 42':^30}")
print('*' *30) 

ladoA = int(input('Digite o tamanho do lado A'))
ladoB = int(input('Digite o tamanho do lado B'))
ladoC = int(input('Digite o tamanho do lado C'))

if ladoA + ladoB >= ladoC and ladoA + ladoC >= ladoB and ladoB + ladoC >= ladoA:
    print(f'Há um triangulo possível com os lados {ladoA}, {ladoB} e {ladoC}')
    if ladoA == ladoB and ladoB ==ladoC:
        tipoTriangulo = 'Equilátero'
    elif ladoA == ladoB or ladoB == ladoC or ladoC ==ladoA:
        tipoTriangulo = 'Isóceles'
    elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
        tipoTriangulo = 'Escaleno'
    print(f'E esse triângulo é do tipo: {tipoTriangulo}')
else:
    print(f'Não há um triangulo possível com os lados {ladoA}, {ladoB} e {ladoC}')
    
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)