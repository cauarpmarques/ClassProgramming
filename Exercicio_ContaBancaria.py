class ContaBancaria:
    def __init__(self, titular, saldo=0 ):
        self.__titular = titular
        self.__saldo = saldo 
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor 
            print(f"O deposito do valor R${valor:.2f} foi realizado com sucesso.")
        else:
            print("O deposito realizado devo ser maior que zero.")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor 
            print(f"O saque realizado do valor R${valor:.2f} foi realizado com sucesso.")
        else:
            print("Saldo insuficente para realizar o saque.")
    
    def verificar_saldo(self):
        print(f"O saldo atual do titular {self.__titular}:R${self.__saldo:.2f}")

#Criando a conta bancaria a partir dos dados informados pelo usuário 
        
def main():
    nome_titular = input("Digite o nome do titular da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))

    conta = ContaBancaria(nome_titular, saldo_inicial)

    while True:
        print("\n Escolha uma das opçoes:")
        print("1. Deposito")
        print("2. Saque")
        print("3. Ver saldo")
        print("4. Sair")
    
        opcao_escolhida = input("Escolha a opção desejada: ")

        if opcao_escolhida == '1':
            valor_depositado = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_depositado)

        elif opcao_escolhida == '2':
            valor_sacado = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_sacado)

        elif opcao_escolhida == '3':
            conta.verificar_saldo()

        elif opcao_escolhida == '4':
            print("Até a próxima! Encerrando o programa...")
            break
        else:
            print("A o opção escolhida está invalida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()









