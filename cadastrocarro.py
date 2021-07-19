from carro import Carro
from piloto import Piloto
from cadastropiloto import CadastroPiloto

carros = []


class CadastroCarro(Carro):
    def __init__(self, on, vel, marca, modelo, aceleracao, velocMax, pil: Piloto, tpDirecao) -> None:
        super().__init__(on, vel, marca, modelo, aceleracao, velocMax, pil, tpDirecao)

    def incluir():
        marca = input('Marca: ')
        modelo = input('Modelo: ')
        on = bool(input('Ligado/Desligado: '))
        vel = float(input('Velocidade: '))
        aceleracao = float(input('Aceleração: '))
        velocMax = float(input('Velocidade Máxima: '))
        tpDirecao = input('Tipo de Direção: ')
        pil = CadastroPiloto.incluir()
        c = CadastroCarro(on, vel, marca, modelo, aceleracao,
                          velocMax, pil, tpDirecao)
        carros.append(c)
        return c

    def remover(marca):
        status = False
        if len(carros) == 0:
            print('Não há registros em Carros.')
        else:
            for idx, carro in enumerate(carros):
                if str(marca) == str(carro.marca):
                    del(carros[idx])
                    print(f'Carro {marca} removido.')
                    status = True
                else:
                    print(f'Carro {marca} não encontrado.')
        return status

    def consultar(marca):
        if len(carros) == 0:
            print('Não há registros em Carros.')
        else:
            for carro in carros:
                if str(marca) == str(carro.marca):
                    print(f'Carro {marca} se encontra nos registros.')
                    return carro
                else:
                    print(f'Carro {marca} não consta nos registros.')

    def atualizar(marca):
        if len(carros) == 0:
            print('Não há registros em Carros.')
        else:
            for idx, carro in enumerate(carros):
                if str(marca) == str(carro.marca):
                    print(
                        f'Carro {marca} encontrado em nossos registros.\nVamos atualizar os dados: ')
                    marca = input('Marca: ')
                    modelo = input('Modelo: ')
                    on = super().ligar()
                    vel = float(input('Velocidade: '))
                    aceleracao = float(input('Aceleração: '))
                    velocMax = float(input('Velocidade Máxima: '))
                    tpDirecao = input('Tipo de Direção: ')
                    pil = CadastroPiloto.incluir()
                    c_aux = CadastroCarro(on, vel, marca, modelo, aceleracao,
                                          velocMax, pil, tpDirecao)
                    carros[idx] = c_aux
                    print('Carro atualizado.')
            else:
                print(f'Carro {marca} não consta nos registros.')


def main():
    carro1 = CadastroCarro.incluir()
    print(carro1.__dict__)


if __name__ == '__main__':
    main()
