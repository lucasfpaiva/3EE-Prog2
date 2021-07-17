from carro import Carro
from piloto import Piloto

carros = []


class CadastroCarro(Carro):
    def __init__(self, on, vel, marca, modelo, aceleracao, velocMax, pil: Piloto, tpDirecao) -> None:
        super().__init__(on, vel, marca, modelo, aceleracao, velocMax, pil, tpDirecao)

    def incluir():
        pass

    def remover():
        pass

    def consultar():
        pass

    def atualizar():
        pass


def main():
    pass


if __name__ == '__main__':
    main()
