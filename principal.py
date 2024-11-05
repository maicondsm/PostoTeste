from Frentista import Frentista
from bombaCombustivel import bombaCombustivel 

nome = input("Qual nome: ")
cpf = input("CPF: ")
frentista1 = Frentista(nome, cpf, '00012')

while True:
    print('=============================')
    print("Tipo de combustível:")
    print("\n[1] - Gasolina")
    print("[2] - Álcool")
    print("[0] - SAIR")
    print('=============================')
    
    opcao = int(input("Qual tipo de combustível deseja abastecer (1 ou 2): "))
    if opcao == 1:
        print("Gasolina selecionada")
        bomba1 = bombaCombustivel("Gasolina", 5.60, 1000)
        bomba1.frentista = frentista1
        break
    elif opcao == 2:
        print("Álcool selecionado")
        bomba1 = bombaCombustivel("Álcool", 4.00, 1500)
        bomba1.frentista = frentista1
        break
    elif opcao == 0:
        print("Encarrando software, volte sempre!!")
        exit()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

while True:
    print('=============================')
    print('Forma de abastecimento:')
    print('[1] - Por litro')
    print('[2] - Por valor (R$)')
    print("[0] - SAIR")
    print('=============================')
    
    abastecer = int(input("Como prefere abastecer (1 ou 2): "))
    
    if abastecer == 1:
        litros = float(input("Quantos litros deseja abastecer: "))
        bomba1.abastecerPorLitro(litros)
        break
    elif abastecer == 2:
        valor = float(input("Quanto R$ deseja colocar: "))
        bomba1.abastecerPorValor(valor)
        break
    elif abastecer== 0:
        print("Operação cancelada!")
        print("Encerrando... Volte sempre!")
        exit()
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Exibindo o extrato
bomba1.extrato()
