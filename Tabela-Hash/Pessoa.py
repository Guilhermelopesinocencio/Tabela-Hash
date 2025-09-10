class Pessoa:
    def __init__(self, cpf, nome, idade):  # Construtor da classe
        self.cpf = cpf                      # Atributo CPF (chave única)
        self.nome = nome                    # Atributo nome da pessoa
        self.idade = idade                  # Atributo idade da pessoa
    
    def __str__(self):                     # Método para representação em string
        return f"CPF: {self.cpf}, Nome: {self.nome}, Idade: {self.idade}"
    
    def __repr__(self):                    # Método para representação oficial
        return self.__str__()
