from Frentista import Frentista
from bombaCombustivel import bombaCombustivel 

nome = input("Qual nome: ")
cpf = input("CPF: ")
frentista1 = Frentista(nome, cpf,'00012')

bomba1 = bombaCombustivel("Gasolina", 5.60, 1000) 
bomba1.frentista = frentista1

print('=============================')
print('Forma de abastecimento: ')
print('[1] - Por litro')
print('[2] - Por valor (R$)')
print('=============================')
abastecer = int(input("Como prefere abastecer (1 ou 2): "))
if abastecer == 1:
    litros = float(input("Quantos litros deseja abastecer: "))
    bomba1.abastecerPorLitro(litros)

elif abastecer == 2:
    valor = float(input("Quanto R$ deseja colocar: "))
    bomba1.abastecerPorValor(valor)

# Exibindo o extrato
bomba1.extrato()