class Tarefas:
    def __init__(self, descricao, status):
        self.__descricao = descricao
        self.__status = status

    def get_descricao(self):
        return self.__descricao
    def get_status(self):
        return  self.__status

    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_status(self, status):
        self.__status = status
