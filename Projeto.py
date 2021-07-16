# projeto 2 unidade Programação 2 Bacharelado em Engenharia Elétrica
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        self.__idade = valor


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
        return super().acelerar()


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
pil1 = Piloto('Jose', 21, 1)
pil2 = Piloto('Joaquim', 35, 1)
pil3 = Piloto('Henrique', 32, 1)
carros = []
carros.append(Carro(0, 0, 'Porsche', '1954', 10, 55, pil1, 'Hidráulica'))
carros.append(Carro(0, 0, 'McLaren', '2001', 10, 50, pil2, 'Hidráulica'))
carros.append(Carro(0, 0, 'Mustang', '1900', 10, 50, pil3, 'Hidráulica'))
# -----------------------------------

carroVencedor = ''
menor_Tempo = 0
contador = 0
for carroAtual in carros:
    distPercorrida = 0
    contador = 0
    while distPercorrida < 1000:
        contador += 1
        carroAtual.acelerar()
        distPercorrida += carroAtual.veloc
    if menor_Tempo == 0:
        menor_Tempo = contador
    elif contador < menor_Tempo:
        menor_Tempo = contador
        carroVencedor = f'{carroAtual.marca} {carroAtual.modelo}'

print(f'O carro vencedor foi: {carroVencedor}')
