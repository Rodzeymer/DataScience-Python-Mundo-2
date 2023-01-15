# Mudando um pouco de desafio, agora um teste para usar um módulo que permita o sistema "atrasar" a 
# execução de um algoritmo, que coloca uma espera para executar a próxima instrução, aqui simulamos uma
# queima de fogos, em que há uma contagem regressiva e após isso o que acontece numa queima de fogos típica
# de um final de ano

print('*' *30)
print("{'Python Mundo 2 - Desafio 46':^30}")
print('*' *30)

from time import sleep

comecar = input('Aperte enter para começar a contagem dos fogos')

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Fogos explodindo')
sleep(0.5)
print('Barulho ensurdecedor')
sleep(0.5)
print('Cachorro latindo')
sleep(0.5)
print('Criança chorando')
sleep(0.5)
print('Feliz ano novo')
sleep(0.5)
print('Gente se abraçando')
sleep(0.5)
print('Silêncio finalmente')
print('*' *30)
print(f"{'FIM':^30}")
print('*' *30)