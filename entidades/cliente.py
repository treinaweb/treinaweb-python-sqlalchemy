class Cliente():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @idade.setter
    def idade(self, idade):
        self.__idade = idade