from veiculo import Veiculo
from piloto import Piloto


class Carro(Veiculo):
    def __init__(self, on, vel, marca, modelo, aceleracao, velocMax, pil: Piloto, tpDirecao) -> None:
        super().__init__(on, vel, marca, modelo, aceleracao, velocMax, pil)
        self.__tpDirecao = tpDirecao

    @property
    def tpDirecao(self):
        return self.__tpDirecao

    @tpDirecao.setter
    def tpDirecao(self, valor):
        self.__tpDirecao = valor

    def acelerar(self):
        return super().acelerar() + 10
