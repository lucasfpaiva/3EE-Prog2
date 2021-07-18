from moto import Moto
from piloto import Piloto
from cadastropiloto import CadastroPiloto

motos = []


class CadastroMoto(Moto):
    def __init__(self, on, veloc, marca, modelo, aceleracao, peso, velocMax, pil: Piloto, tpGuidao) -> None:
        super().__init__(on, veloc, marca, modelo, aceleracao, peso, velocMax, pil, tpGuidao)

    def incluir():
        marca = input('Marca: ')
        modelo = input('Modelo: ')
        on = bool(input('Ligado/Desligado: '))
        vel = float(input('Velocidade: '))
        aceleracao = float(input('Aceleração: '))
        velocMax = float(input('Velocidade Máxima: '))
        tpGuidao = input('Tipo de Direção: ')
        pil = CadastroPiloto.incluir()
        m = CadastroMoto(on, vel, marca, modelo, aceleracao,
                         velocMax, pil, tpGuidao)
        motos.append(m)
        return m

    def remover(marca):
        status = False
        if len(motos) == 0:
            print('Não há registros em Motos.')
        else:
            for idx, moto in enumerate(motos):
                if str(marca) == str(moto.marca):
                    del(motos[idx])
                    print(f'Moto {marca} removida.')
                    status = True
                else:
                    print(f'Moto {marca} não encontrada.')
        return status

    def consultar(marca):
        if len(motos) == 0:
            print('Não há registros em Motos.')
        else:
            for moto in motos:
                if str(marca) == str(moto.marca):
                    print(f'Moto {marca} se encontra nos registros.')
                    return moto
                else:
                    print(f'Moto {marca} não consta nos registros.')

    def atualizar(marca):
        if len(motos) == 0:
            print('Não há registros em motos.')
        else:
            for idx, moto in enumerate(motos):
                if str(marca) == str(moto.marca):
                    print(
                        f'Moto {marca} encontrado em nossos registros.\nVamos atualizar os dados: ')
                    marca = input('Marca: ')
                    modelo = input('Modelo: ')
                    on = bool(input('Ligado/Desligado: '))
                    vel = float(input('Velocidade: '))
                    aceleracao = float(input('Aceleração: '))
                    velocMax = float(input('Velocidade Máxima: '))
                    tpDirecao = input('Tipo de Direção: ')
                    pil = CadastroPiloto.incluir()
                    m_aux = CadastroMoto(on, vel, marca, modelo, aceleracao,
                                         velocMax, pil, tpDirecao)
                    motos[idx] = m_aux
                    print('Moto atualizado.')
            else:
                print(f'Moto {marca} não consta nos registros.')


def main():
    pass


if __name__ == '__main__':
    main()
