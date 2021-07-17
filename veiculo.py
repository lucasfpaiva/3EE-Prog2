from piloto import Piloto


class Veiculo:
    def __init__(self, on, vel, marca, modelo, aceleracao, velocMax, pil: Piloto) -> None:
        self.__on = on
        self.__veloc = float(vel)
        self.__marca = marca
        self.__modelo = modelo
        self.__aceleracao = float(aceleracao)
        self.__velocMax = velocMax
        self.__piloto = pil

    @property
    def piloto(self):
        return self.__piloto

    @piloto.setter
    def piloto(self, valor):
        self.__piloto = valor

    @property
    def on(self):
        return self.__on

    @on.setter
    def on(self, valor):
        self.__on = valor

    @property
    def veloc(self):
        return float(self.__veloc)

    @veloc.setter
    def veloc(self, valor):
        if valor > 0 and valor <= self.__velocMax:
            self.__veloc = valor
        else:
            self.__veloc = 0

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor

    @property
    def aceleracao(self):
        return self.__aceleracao

    @aceleracao.setter
    def aceleracao(self, valor):
        self.__aceleracao = valor

    @property
    def velocMax(self):
        return float(self.__velocMax)

    @velocMax.setter
    def velocMax(self, valor):
        self.__velocMax = valor

    def partida(self):
        self.__on = True

    def acelerar(self):
        self.veloc += self.aceleracao*self.piloto.proficiencia

        if self.veloc > self.velocMax:
            self.veloc = self.velocMax

    def frenagem(self):
        if self.veloc < 0:
            self.veloc = 0
        else:
            self.veloc -= self.aceleracao*10
