from agenda import Agenda
from contatos import Contatos
from tarefas import Tarefas

class Menu:
    def __init__(self):
        self.agenda = []
        self.contatos = []
        self.tarefas = []

    def cadastra_contato(self,):
        nome = input("Qual o nome completo a ser cadastrado: ")
        telefone = input("Digite o numero de telefone:")
        novo_contato = Contatos(nome, telefone)
        self.contatos.append(novo_contato)

    def lista_contato(self):
        for item in self.contatos:
            print("Contato: " + str(item.get_nome))
            print("Telefone: " + str(item.get_telefone))

    def exclui_contato(self):
        contato = input("Qual contato será excluído?")
        for item in self.contatos:
            if(item.get_nome == contato):
                self.contatos.remove(item)
                print("Contato excluido")

    def cadastra_tarefa(self):
        descricao = input("Descreva a tarefa: ")
        status = True
        nova_tarefa = Tarefas(descricao, status)
        self.tarefas.append(nova_tarefa)

    def exclui_tarefa(self):
        tarefa = input("Qual tarefa será excluida?")
        for item in self.tarefas:
            if(item.get_tarefa == tarefa):
                self.tarefas.remove(item)

    def lista_tarefa(self):
        for item in self.tarefas:
            print("Tarefa: "+ str(item.get_tarefa))
            print("Status: " + str(item.get_staus))

    def menu_opcoes(self):
        print("Escolhas as opcoes abaixo")
        print("Opcao 1 - Cadastrar contatos")
        print("Opcao 2 - Lista de contatos")
        print("Opcao 3 - Excluir contatos")
        print("Opcao 4 - Incluir nova tarefa")
        print("Opcao 5 - Lista de taredas")
        print("Opcao 6 - Excluir tarefa")
        print("Opcao 8 - Fechar agenda")

    def menu_principal(self):
        while True:
            self.menu_opcoes()
            resposta = input("Escolha a opcao desejada: ")
            print(resposta)
            if(resposta == "1"):
                self.cadastra_contato()
            elif(resposta == "2"):
                self.lista_contato()
            elif(resposta == "3"):
                self.exclui_contato()
            elif(resposta == "4"):
                self.cadastra_tarefa()
            elif(resposta == "5"):
                self.lista_tarefa()
            elif(reposta == "6"):
                self.exclui_tarefa()
            elif(respota == "8"):
                print("Agenda fechada")
                return
Menu().menu_opcoes()



