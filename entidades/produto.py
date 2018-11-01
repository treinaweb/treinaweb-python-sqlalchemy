class Produto():
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @valor.setter
    def valor(self, valor):
        self.__valor = valor