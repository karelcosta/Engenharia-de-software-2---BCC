class PessoaFisica:
    def __init__(self, cpf) -> None:
        self.CPF = cpf

class PessoaJuridica:
    def __init__(self, cnpj) -> None:
        self.CNPJ = cnpj

class Pessoa:
    def get_PessoaFisica(self, cpf) -> PessoaFisica:
        self.pessoa = PessoaFisica(cpf)
    def PessoaJuridica(self, cnpj) -> PessoaJuridica:
        self.pessoa = PessoaJuridica(cnpj)

class Imovel:
  def __init__(self, valor:float, endereço:str):
    self.aluguel = valor
    self.endereço = endereço
    self.inquilino = None
    # Status indica se o imovel esta ou não alugado
    self.status = False

class casa(Imovel):
    def __init__(self, valor: float, endereço: str, prom_energ:float = 0):
        super().__init__(valor, endereço)
        self.prom_energ = prom_energ

class quarto_escritorio(Imovel):
    def __init__(self, valor: float, endereço: str, complemento:str):
        super().__init__(valor, endereço)
        self.complemento = complemento

class Imobiliaria(PessoaJuridica):
    def __init__(self, cnpj) -> None:
        super().__init__(cnpj)
        self.imoveis = []
    
    def procurarImovel(self):
        disponiveis = []
        for i in self.imoveis:
            if i.status:
                disponiveis.append(i)
        return disponiveis
    
    def alugar(self, inquilino:Pessoa, imovel:Imovel, promoçãoAluguel:float, promoçãoEnergia:float):
        imovel.inquilino = inquilino
        imovel.aluguel -= imovel.aluguel*promoçãoAluguel    
    
    def novoImovel(self, novoImovel):
        self.imoveis.append(novoImovel)