from moto import Moto
from piloto import Piloto

motos = []


class CadastroMoto(Moto):
    def __init__(self, on, veloc, marca, modelo, aceleracao, peso, velocMax, pil: Piloto, tpGuidao) -> None:
        super().__init__(on, veloc, marca, modelo, aceleracao, peso, velocMax, pil, tpGuidao)

    def incluir():
        pass

    def remover(nome):
        pass

    def consultar(nome):
        pass

    def atualizar(nome):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
