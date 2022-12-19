ladoA = int(input('Digite o tamanho do lado A'))
ladoB = int(input('Digite o tamanho do lado B'))
ladoC = int(input('Digite o tamanho do lado C'))

if ladoA + ladoB >= ladoC and ladoA + ladoC >= ladoB and ladoB + ladoC >= ladoA:
    print('Há um triangulo possível com os lados {}, {} e {}'.format(ladoA, ladoB, ladoC))
    if ladoA == ladoB and ladoB ==ladoC:
        tipoTriangulo = 'Equilátero'
    elif ladoA == ladoB or ladoB == ladoC or ladoC ==ladoA:
        tipoTriangulo = 'Isóceles'
    elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
        tipoTriangulo = 'Escaleno'
    print('E esse triângulo é do tipo: {}'.format(tipoTriangulo))
else:
    print('Não há um triangulo possível com os lados {}, {} e {}'.format(ladoA, ladoB, ladoC))