# projeto 2 unidade Programação 2 Bacharelado em Engenharia Elétrica
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome


class Piloto(Pessoa):
    def __init__(self, nome, idade, prof):
        super().__init__(nome, idade)
        self.proficiencia = prof


class Veiculo:
    def __init__(self, on, vel, marca, modelo, aceleracao, peso, velocMax) -> None:
        self.__on = on
        self.__veloc = vel
        self.__marca = marca
        self.__modelo = modelo
        self.__aceleracao = aceleracao
        self.__peso = peso
        self.__velocMax = velocMax

    @property
    def on(self):
        return self.__on

    @on.setter
    def on(self, valor):
        self.__on = valor

    @property
    def veloc(self):
        return self.__veloc

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
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, valor):
        self.__peso = valor

    @property
    def velocMax(self):
        return self.__velocMax

    @velocMax.setter
    def velocMax(self, valor):
        self.__velocMax = valor

    def partida(self):
        self.__on = True

    def acelerar(self):
        self.veloc += self.aceleracao
        if self.veloc > self.velocMax:
            self.veloc = self.velocMax

    def frenagem(self):
        if self.veloc < 0:
            self.veloc = 0
        else:
            self.veloc -= 5


class Carro(Veiculo):
    def __init__(self, on, veloc, marca, modelo, aceleracao, peso, velocMax, tpDirecao, pil: Piloto) -> None:
        super().__init__(on, veloc, marca, modelo, aceleracao, peso, velocMax)
        self.__tpDirecao = tpDirecao
        self.piloto = pil

    @property
    def tpDirecao(self):
        return self.__tpDirecao

    @tpDirecao.setter
    def tpDirecao(self, valor):
        self.__tpDirecao = valor

    def acelerar(self):
        return super().acelerar() * self.piloto.proficiencia


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


# ----------------------------------
carros = []
carros.append(Carro(0, 0, 'Porsche', '1954', 10, 1500, 55, 'Hidráulica'))
carros.append(Carro(0, 0, 'McLaren', '2001', 7, 2500, 60, 'Hidráulica'))
carros.append(Carro(0, 0, 'Mustang', '1900', 15, 1700, 56, 'Hidráulica'))
# -----------------------------------

for carroAtual in carros:
    distPercorrida = 0
    carroVencedor = ''
    while distPercorrida < 1000:
        carroAtual.acelerar(0.95)
        distPercorrida += carroAtual.veloc
