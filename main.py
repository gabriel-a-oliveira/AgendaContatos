class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, nome, telefone):
        contato = Contato(nome, telefone)
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso.")

    def exibir_contatos(self):
        if not self.contatos:
            print("Nenhum contato encontrado.")
        else:
            print("\nLista de contatos:")
            for contato in self.contatos:
                print(contato)

    def editar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                novo_telefone = input("Digite o novo telefone: ")
                contato.telefone = novo_telefone
                print(f"Contato {nome} atualizado com sucesso!")
                return
        print(f"Contato {nome} não encontrado.")

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {nome} excluído com sucesso!")
                return
        print(f"Contato {nome} não encontrado.")

class Menu:
    def __init__(self):
        self.agenda = Agenda()

    def exibir_menu(self):
        opcoes = {
            "1": self.adicionar_contato,
            "2": self.exibir_contatos,
            "3": self.editar_contato,
            "4": self.excluir_contato,
            "5": self.sair,
        }

        while True:
            print("\n--- Agenda de Contatos ---")
            print("1. Adicionar Contato")
            print("2. Exibir Contatos")
            print("3. Editar Contato")
            print("4. Excluir Contato")
            print("5. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao in opcoes:
                opcoes[opcao]()
                if opcao == "5":
                    break
            else:
                print("Opção inválida. Tente novamente.")

    def adicionar_contato(self):
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        self.agenda.adicionar_contato(nome, telefone)

    def exibir_contatos(self):
        self.agenda.exibir_contatos()

    def editar_contato(self):
        nome = input("Digite o nome do contato que deseja editar: ")
        self.agenda.editar_contato(nome)

    def excluir_contato(self):
        nome = input("Digite o nome do contato que deseja excluir: ")
        self.agenda.excluir_contato(nome)

    def sair(self):
        print("Saindo da agenda. Até logo!")

menu = Menu()
menu.exibir_menu()
