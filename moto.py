from abc import abstractmethod
from veiculo import Veiculo
from piloto import Piloto


class Moto(Veiculo):
    def __init__(self, on, veloc, marca, modelo, aceleracao, peso, velocMax, pil: Piloto, tpGuidao) -> None:
        super().__init__(on, veloc, marca, modelo, aceleracao, peso, velocMax)
        self.__tpGuidao = tpGuidao

    @property
    def tpGuidao(self):
        return self.__tpGuidao

    @tpGuidao.setter
    def tpGuidao(self, valor):
        self.__tpGuidao = valor

    def acelerar(self):
        return super().acelerar() + 5

    @abstractmethod
    def ligar(self):
        self.on = True
