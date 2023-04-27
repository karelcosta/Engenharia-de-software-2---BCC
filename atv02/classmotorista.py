class Motorista():

    def __init__(self, nome, rg, cpf, cnh):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.cnh = cnh

    # Função para cadastrar motorista
    def cadastrar_motorista(self, nome, rg, cpf, cnh):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.cnh = cnh

    # Função para editar motorista
    def editar_motorista(self, op):
        if op == 1:
            nome = input("Digite o novo nome do motorista: ")
            self.nome = nome
        elif op == 2:
            rg = input("Digite o novo rg do motorista: ")
            self.rg = rg
        elif op == 3:
            cpf = input("Digite o novo cpf do motorista: ")
            self.cpf = cpf
        elif op == 4:
            cnh = input("Digite o novo cnh do motorista: ")
            self.cnh = cnh
        else:
            print("Opção inválida.")

    def pesquisar_motorista(self):
        print(
            f"Nome: {self.nome}.\nRG: {self.rg}.\nCPF: {self.cpf}.\nCNH: {self.cnh}."
        )
