class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome 
        self.idade = idade 
        self.peso = peso
    
    def imprimir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso} kg")

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_peso(self):
        return self.peso

    def atualizar_informacoes(self, nome=None, idade=None, peso=None):
        if nome:
            self.nome = nome
        if idade:
            self.idade = idade
        if peso:
            self.peso = peso

   
# Exemplo de uso da classe
pessoa1 = Pessoa("Cauã", 19, 59)

# Imprimir informações
pessoa1.imprimir_informacoes()

# Atualizar informações
pessoa1.atualizar_informacoes(idade=20, peso=65)

# Imprimir informações atualizadas
pessoa1.imprimir_informacoes()

