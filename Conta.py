class Conta:
    def __init__(self,agencia,numero):
        self.agencia=agencia
        self.numero=numero
        self.limite= 1000 # O limite é R$1000
        self.saldo= 0 #Quando cria uma conta incialmente ela tem 0
        self.historico = [] #Lista para armazenar as operações na conta

    def verificar_saldo(self):
        print(f"Olá, a conta {self.numero} tem R${self.saldo:.2f} de saldo disponível.")#Verificação rápida do saldo
    
    
    def extrato(self): #É um método que mostra o extrato da conta, mostrando as operações realizadas, seus valores e saldos.
        print(f"Extrato da conta {self.numero} - Agência {self.agencia}")
        print("\tOperação\tValor\tSaldo")
        for op in self.historico: #Percorrendo a lista self.historico, em que cada operação realizada, a variável op assume.
            if op[0] == 'Depósito':
                print(f"\tDepósito\t{op[1]:.2f}\t{self.saldo:.2f}")
            elif op[0] == 'Saque':
                print(f"\tSaque\t\t{op[1]:.2f}\t{self.saldo:.2f}")
            elif op[0] == 'Transferência':
                if len(op) == 3: #Verifica se existe um terceiro elemento na tupla
                    print(f"\tTransferência\t{op[1]:.2f}\t{self.saldo:.2f}\tDestino: {op[2].numero}")
            else:
                if len(op) == 3:
                    print(f"\tRecebido\t{op[1]:.2f}\t{self.saldo:.2f}\tOrigem: {op[2].numero}")
                    
    def sacar(self, valor):
        if  self.saldo <= 0 or valor <=0 : #Não pode sacar valor negativo
            print("Não pode sacar pois não tem valor na sua conta e/ou pode ser valor negativo.")
        elif self.limite < valor or valor > self.saldo: #Não pode ser maior que o limite ou maior que o saldo
            print("Saldo insuficiente")
        else:
            self.saldo -=valor
            self.historico.append(("Saque:", valor))
            
    def depositar(self, valor):
        if valor > self.limite or self.saldo + valor > self.limite:
            print(f"Não pode, pois o valor máximo é R${self.limite:.2f}")
        elif  valor <= 0:
            print("Não pode depositar valor negativo ou nada.")
        else:
            self.saldo += valor
            self.historico.append(("Depósito:", valor))

    def fazer_transferencia(self, valor, destino):
        if valor <= 0:
            print("Valor inválido para transferência.")
            
        elif self.saldo < valor:
            print("Saldo insuficiente.")
        
        else:
            self.saldo -= valor
            self.historico.append(('Transferência', valor, destino))
            destino.saldo += valor
            destino.historico.append(('Recebido', valor, self))
            print(f"Transferência de R${valor:.2f} realizada com sucesso.")
    def encerra_conta(self):
        if self.saldo != 0:
            print("Conta não pode ser encerrada. Saldo não é igual a zero.")
        else:
            self.historico.append(('E', 0))
            print("Conta encerrada com sucesso.")

P1 = Conta(1234,5678)
P2 = Conta(2134,3453)

P1.depositar(400)
P1.depositar(501)
P1.verificar_saldo()
P1.sacar(-44)
P1.fazer_transferencia(10,P2)
P2.verificar_saldo()
P1.extrato()
P2.extrato()
