from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, on, veloc, marca, modelo, aceleracao, peso, velocMax, tpGuidao) -> None:
        super().__init__(on, veloc, marca, modelo, aceleracao, peso, velocMax)
        self.__tpGuidao = tpGuidao

    @property
    def tpGuidao(self):
        return self.__tpGuidao

    @tpGuidao.setter
    def tpGuidao(self, valor):
        self.__tpGuidao = valor
