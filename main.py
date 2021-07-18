from cadastrocarro import CadastroCarro
import sys

# ----------------------------------
carros = []

sys.stdin = open('data.txt', 'r')

quantCarros = int(input('Informe a quantidade de carros: '))
print(f'Vamos cadastrar {quantCarros} carros e seus pilotos:\n')

while quantCarros:
    c = CadastroCarro.incluir()
    carros.append(c)
    quantCarros -= quantCarros
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

    if contador < menor_Tempo:
        menor_Tempo = contador

st = f'\n\nVencedor: {carroAtual.marca}\n'
st += f'Modelo: {carroAtual.modelo}\n'
st += f'Pilotado por {carroAtual.piloto.nome}\n'
st += f'Distância percorrida: {distPercorrida:.2f} km.\n'
st += f'Tempo: {menor_Tempo:.2f} h.\n'
st += f'Velocidade média: {distPercorrida/menor_Tempo:.2f} km/h.'

print(st)
