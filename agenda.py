class Agenda:
    def __init__(self, nome_proprietario, ano):
        self.__nome_proprietario = nome_proprietario
        self.__ano = ano

    def get_nome_proprietario(self):
        return self.__nome_proprietario
    def get_ano(self):
        return self.__ano

    def set_nome_proprietario(self, nome_proprietario):
        self.__nome_proprietario = nome_proprietario
    def set_ano(self, ano):
        self.__ano = ano

