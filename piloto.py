from pessoa import Pessoa


class Piloto(Pessoa):
    def __init__(self, nome, idade, prof):
        super().__init__(nome, idade)
        self.__proficiencia = float(prof)

    @property
    def proficiencia(self):
        return float(self.__proficiencia)

    @proficiencia.setter
    def proficiencia(self, valor):
        self.__proficiencia = float(valor)
