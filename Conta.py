class Conta:
    def __init__(self,agencia,numero):
        self.agencia=agencia
        self.numero=numero
        self.limite= 1000
        self.saldo= 0
        self.historico = []

    def verificar_saldo(self):
        return f"Você tem {self.saldo} de saldo disponível."
    
    def extrato(self):
        pass
    def sacar(self, valor):
        if  self.saldo <= 0:
            print("Não pode sacar pois não tem valor na sua conta")
        elif self.saldo + self.limite < valor:
            print("Saldo insuficiente")
        else:
            self.saldo -=valor
            self.historico.append(("Saque:", valor))
    def depositar(self, valor):
        if self.saldo > self.limite:
            print("Não pode, pois o valor máximo é R$1000")
        elif  valor <= 0:
            print("Não pode depositar valor negativo")
        else:
            self.saldo += valor

    def fazer_transferencia(self):
        pass
    def encerrar(self):
        pass

Gabriel = Conta(1234,5678)

Gabriel.depositar(200)
print(Gabriel.verificar_saldo())
Gabriel.sacar(300)
print(Gabriel.verificar_saldo())
Gabriel.historico()
