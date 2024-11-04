from datetime import datetime
class bombaCombustivel:
    def __init__(self, tipocombustivel, valorlitro, estoquecombustivel):
        self.tipocombustivel = tipocombustivel
        self.valorlitro = valorlitro
        self.estoquecombustivel = estoquecombustivel
        self.frentista = None
        self.resultadoLitro = None
        self.resultadoValor = None
        self.dataHora = None

    def FormataReal(self, valor):
        valor = float(valor)
        valor_formatado = "{:,.2f}".format(valor).replace(".", ",")
        return valor_formatado

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorlitro
        self.estoquecombustivel -= litros_abastecidos
        self.resultadoValor = f'{litros_abastecidos:.2f} litros abastecidos. \nValor a pagar: R$ {self.FormataReal(valor)}'
        self.registrarDataHora()

    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valorlitro
        self.estoquecombustivel -= litros
        self.resultadoLitro = f'{litros:.2f} litros abastecidos. \nValor a pagar: R$ {self.FormataReal(valor_a_pagar)}'
        self.registrarDataHora()

    def alterarValor(self, valor):
        self.valorlitro = valor

    def registrarDataHora(self):
        self.dataHora = datetime.now()

    def extrato(self):
        print('\n===============================')
        print('          Nota Fiscal          ')
        print('===============================')

        if self.frentista:
            print('Frentista responsavel: ')
            print(f'Nome: {self.frentista.nome}')
            print(f'CPF: {self.frentista.cpf}')
        else:
            print(f'Responsavel: Não especificado')

        print(f'\n===============================')
        print(f'         Posto De Teste          ')
        print(f'===============================')
        if self.resultadoValor:
            print(f"\nLitros abastecidos: {self.resultadoValor} reais")
        elif self.resultadoLitro:
            print(f"\nLitros abastecidos: {self.resultadoLitro} reais")
        else:
            print("Volte sempre!")
        if self.dataHora:
            print(f'\nTipo combustivel:    {self.tipocombustivel}')
            print(f'\nData/Hora abastecimento: {self.dataHora.strftime("%d/%m/%Y %H:%M:%S")}')
        else:
            print("\nData/Hora abastecimento: Não disponível")
        print("Volte sempre!")
        print(f'===============================')


