import classveiculo
import classmotorista

veiculos = [classveiculo.Veiculo("BMW","I8",2023,123,321,"preto",0)]
motoristas = [classmotorista.Motorista("benjamin", 123, 321, 98)]
viagens = [classveiculo.viagem('31/02/2012', veiculos[0], 'Caxias', 'Dubai', motoristas[0])]
manutencoes = [classveiculo.manutencao(12, '123bc', 734.5)]
abastecimentos = [classveiculo.Abastecimento(17, '123bc', 134.5)]

while True:
  print('Selecione uma opção:')
  print('1. Gerenciamento de Motoristas')
  print('2. Gerenciamento de Veículos')
  print('3. Gerenciamento de Viagem')
  print('4. manutenção')
  print('5. abastecimento')
  print('6. Relatório')
  print('7. Sair')

  opcao = int(input())
  # Menu motorista
  if opcao == 1:
    print('Selecione uma opção:')
    print('1. Cadastrar Novo Motorista')
    print('2. Pesquisar Motorista')
    print('3. Editar Motorista')
    print('4. Deletar Motorista')
    sub_opcao = int(input())

    if sub_opcao == 1:
      nome = input("Digite o seu nome: ")
      rg = int(input("Digite seu rg: "))
      cpf = int(input("Digite seu cpf: "))
      cnh = int(input("Digite seu cnh: "))
      motoristas.append(classmotorista.Motorista(nome, rg, cpf, cnh))

    elif sub_opcao == 2:
      cpf = int(input("Digite seu cpf: "))
      for i in motoristas:
        if cpf == i.cpf:
          i.pesquisar_motorista()
    elif sub_opcao == 3:
      cpf = int(input("Digite seu cpf: "))
      for i in motoristas:
        if cpf == i.cpf:
          i.pesquisar_motorista()
          print('Selecione uma opção:')
          print('1. Editar NOME')
          print('2. Editar RG')
          print('3. Editar CPF')
          print('4. Editar CNH')
          op = int(input())
          i.editar_motorista(op)
    elif sub_opcao == 4:
      cpf = int(input("Digite seu cpf: "))
      for i in motoristas():
        if cpf == i.cpf:
          motoristas.remove(i)
    else:
      print('Opção inválida.')

  #menu veiculo
  elif opcao == 2:
    print('Selecione uma opção:')
    print('1. Cadastrar Veículo')
    print('2. Pesquisar Veículo')
    print('3. Editar Veículo')
    print('4. Deletar Veículo')
    print('5. Ver quilometragem de Veículo')
    sub_opcao = int(input())

    if sub_opcao == 1:
      print('Opção selecionada: Cadastrar Veículo')
      marca = input('Informe a marca do carro: ')
      modelo = input('Informe o modelo do carro: ')
      ano = int(input('Informe o ano do carro: '))
      placa = input('Informe a placa do carro: ')
      chassi = input('Informe o chassi do carro: ')
      cor = input('Informe a cor do carro: ')
      quilometragem = float(input('Informe a quilometragem do carro: '))
      veiculos.append(
        classveiculo.Veiculo(marca, modelo, ano, placa, chassi, cor,
                             quilometragem))
    elif sub_opcao == 2:
      aux = True
      print('Opção selecionada: Pesquisar Veículo')
      placa_pesquisa = input('Digite a placa do veiculo: ')

      for veiculo in veiculos:
        if veiculo.placa == placa_pesquisa:
          print(veiculo)
          aux = False
      if aux:
        print('Veiculo não encontrado.')
    elif sub_opcao == 3:
      placa_pesquisa = int(
        input("Digite a placa do veiculo que deseja editar: "))
      for i in veiculos:
        if veiculo.placa == placa_pesquisa:
          print('Selecione uma opção:')
          print("Editar marca:")
          print("Editar modelo:")
          print("Editar ano:")
          print("Editar placa:")
          print("Editar chassi:")
          print("Editar quilometragem:")
          op = int(input())
          i.editar_veiculo(op)

    elif sub_opcao == 4:
        print('Opção selecionada: Deletar Veículo')
        placa_pesquisa = int(
        input("Digite a placa do veiculo que deseja deletar: "))
        for i in veiculos:
            if i.placa == placa_pesquisa:
                veiculos.remove(i)
    elif sub_opcao == 5:
        print('Opção selecionada: Ver quilometragem de Veículo')
        placa_pesquisa = int(input("Digite a placa do veiculo: "))
        for i in veiculos:
            if placa_pesquisa==i.placa:
                print(f"A quilometragem do veiculo é {i.quilometragem}.")
    else:
      print('Opção inválida')

  #menu viagens
  elif opcao == 3:
    print('Selecione uma opção:')
    print('1. Cadastrar Viagem')

    sub_opcao = int(input())

    if sub_opcao == 1:
      print('Opção selecionada: Cadastrar Viagem')
      # Código para cadastrar uma nova viagem
    else:
      print('opição invalida')
  #abastecimentos
  elif opcao == 4:
    print('1. novo abastecimento')
    print('2. ver abastecimentos')
    sub_opcao = int(input(''))

    if sub_opcao == 1:
      data = input("Digite a data: ")
      veiculo = input('informe a placa do veiculo')
      valor = float(input('Digite o valor: '))
      abastecimentos.append(classveiculo.Abastecimento(data, veiculo, valor))
    elif sub_opcao == 2:
      for i in abastecimentos:
        print(f'{i.veiculo} - {i.data} - {i.valor}')
  #manutenção
  elif opcao == 5:
    print('1. nova manutenção')
    print('2. ver manutenções')
    sub_opcao = int(input(''))

    if sub_opcao == 1:
      data = input("Digite a data: ")
      veiculo = input('informe a placa do veiculo')
      valor = float(input('Digite o valor: '))
      manutencoes.append(classveiculo.manutencao(data, veiculo, valor))
    elif sub_opcao == 2:
      for i in abastecimentos:
        print(f'{i.veiculo} - {i.data} - {i.valor}')

  elif opcao == 6:
      print(f"Relatorio:")
      for i in veiculos:
          print(f"Modelo: {i.modelo} - Placa: {i.placa}")
      for i in motoristas:
          print(f"Nome:{i.nome} - CPF: {i.cpf}.")
      for i in viagens:
          print(f"Data: {i.data} - Origem: {i.origem} Destino: {i.destino}.")
      for i in manutencoes:
          print(f"Data: {i.data} - Veiculo: {i.veiculo} - Valor {i.valor}.")
      for i in abastecimentos:
          print(f"Data: {i.data} - Veiculo: {i.veiculo} - Valor {i.valor}.") 
  elif opcao == 7:
    exit()
  else:
    print('Opção inválida')
