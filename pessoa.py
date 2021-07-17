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
