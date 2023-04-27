class Veiculo:
  def __init__(self, marca, modelo, ano, placa, chassi, cor, quilometragem):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.placa = placa
    self.chassi = chassi
    self.cor = cor
    self.quilometragem = quilometragem

  def editar_veiculo(self, op):
    if op == 1:
      print("Digite a nova marca do veiculo: ")
      marca = input()
      self.marca = marca
    elif op == 2:
      print("Digite o novo modelo do veiculo: ")
      modelo = input()
      self.modelo = modelo
    elif op == 3:
      print("Digite o novo ano do veiculo")
      ano = input()
      self.ano = ano
    elif op == 4:
      print("Digite a nova placa do veiculo")
      placa = input()
      self.placa = placa
    elif op == 5:
      print("Digite o novo chassi do veiculo")
      chassi = input()
      self.chassi = chassi
    elif op == 6:
      print("Digite a nova cor do veiculo")
      cor = input()
      self.cor = cor
    elif op == 7:
      print("Digite a nova quilometragem do veiculo")
      quilometragem = input()
      self.quilometragem = quilometragem
    else:
      print("Opção inválida.")

  def pesquisar_veiculo(self):
    print("Marca: {}\nModelo: {}\nAno: {}\nPlaca: {}\nChassi: {}\nCor: {}".format(self.marca, self.modelo, self.ano, self.placa, self.chassi, self.cor))


class Abastecimento:
  def __init__(self, data, veiculo, valor):
    self.data = data
    self.veiculo = veiculo
    self.valor = valor


class manutencao:
  def __init__(self, data, veiculo, valor):
    self.data = data
    self.veiculo = veiculo
    self.valor = valor

class viagem:
  def __init__(self, data, veiculo, origem, destino, motorista):
    self.data = data
    self.veiculo = veiculo
    self.origem = origem
    self.motorista = motorista
    self.destino = destino