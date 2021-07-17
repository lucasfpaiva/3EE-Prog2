from piloto import Piloto
from carro import Carro


# ----------------------------------
pil1 = Piloto('Jose', 21, 0.87)
pil2 = Piloto('Joaquim', 35, 0.92)
pil3 = Piloto('Henrique', 32, 0.95)
carros = []
carros.append(Carro(0, 0, 'Porsche', '1954', 10, 50, pil1, 'Hidráulica'))
carros.append(Carro(0, 0, 'McLaren', '2001', 10, 50, pil2, 'Hidráulica'))
carros.append(Carro(0, 0, 'Mustang', '1900', 10, 56, pil3, 'Hidráulica'))
# -----------------------------------


carroVencedor = ''
menor_Tempo = 0

for carroAtual in carros:
    distPercorrida = 0
    contador = 0

    while distPercorrida < 1000:
        contador += 1
        carroAtual.acelerar()
        distPercorrida += carroAtual.veloc

    if menor_Tempo == 0:
        menor_Tempo = contador
        carroVencedor = f'{carroAtual.marca} {carroAtual.modelo}'

    if contador < menor_Tempo:
        menor_Tempo = contador
        carroVencedor = f'{carroAtual.marca} {carroAtual.modelo}'

print(f'O carro vencedor foi: {carroVencedor}')
