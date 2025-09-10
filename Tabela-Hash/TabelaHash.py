from Pessoa import Pessoa                   
import time                                 

class TabelaHash:
    def __init__(self, tamanho=50):        # Construtor com tamanho padrão 50
        self.tamanho = tamanho              # Tamanho da tabela hash
        self.tabela = [[] for _ in range(tamanho)]  # Lista de listas para encadeamento
        self.colisoes = 0                   # Contador de colisões
        self.total_registros = 0            # Contador total de registros
    
    def funcao_hash(self, cpf):            # Função de hash usando CPF
        if isinstance(cpf, str):            # Se CPF for string
            cpf_limpo = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
            return int(cpf_limpo) % self.tamanho           # Retorna índice da tabela
        else:                               # Se CPF for número
            return cpf % self.tamanho       # Retorna índice da tabela
    
    def inserir(self, pessoa):             # Método para inserir pessoa
        indice = self.funcao_hash(pessoa.cpf)  # Calcula índice usando hash
        
        # Verifica se CPF já existe
        for p in self.tabela[indice]:      # Percorre lista na posição
            if p.cpf == pessoa.cpf:        # Se CPF já existe
                print(f"CPF {pessoa.cpf} já cadastrado!")
                return False
        
        # Conta colisão se posição já tem elementos
        if len(self.tabela[indice]) > 0:   # Se posição não está vazia
            self.colisoes += 1              # Incrementa contador de colisões
        
        self.tabela[indice].append(pessoa) # Adiciona pessoa na lista
        self.total_registros += 1          # Incrementa contador de registros
        print(f"Pessoa {pessoa.nome} cadastrada com sucesso!")
        return True
    
    def buscar(self, cpf):                 # Método para buscar pessoa
        inicio = time.perf_counter()                # Marca tempo inicial
        indice = self.funcao_hash(cpf)     # Calcula índice usando hash
        contador_busca = 0                  # Contador de passos da busca
        
        cpf_str = str(cpf)

        for pessoa in self.tabela[indice]: # Percorre lista na posição
            contador_busca += 1             # Incrementa contador de passos
            if str(pessoa.cpf) == cpf_str:           # Se encontrou a pessoa -- compara sempre como string
                fim = time.perf_counter()           # Marca tempo final
                tempo_busca = (fim - inicio) * 1000  # Calcula tempo em ms

                print(f"Tempo de busca: {tempo_busca:.10f} ms")
                return pessoa
        
        print("Pessoa não encontrada!")
        return None


    def excluir(self, cpf):                # Método para excluir pessoa
        indice = self.funcao_hash(cpf)     # Calcula índice usando hash
        
        for i, pessoa in enumerate(self.tabela[indice]):  # Percorre lista com índice
            if pessoa.cpf == cpf:           # Se encontrou a pessoa
                pessoa_removida = self.tabela[indice].pop(i)  # Remove da lista
                self.total_registros -= 1   # Decrementa contador de registros
                print(f"Pessoa {pessoa_removida.nome} removida com sucesso!")
                return True
        
        print("Pessoa não encontrada para exclusão!")
        return False
    
    def imprimir_tabela(self):             # Método para imprimir tabela completa
        print("\n" + "="*60)
        print("TABELA HASH COMPLETA")
        print("="*60)
        
        for i, lista in enumerate(self.tabela):  # Percorre todas as posições
            if lista:                       # Se posição tem elementos
                print(f"Posição {i:2d}: {len(lista)} registro(s)")
                for pessoa in lista:        # Percorre pessoas na posição
                    print(f"         {pessoa}")
            else:                           # Se posição está vazia
                print(f"Posição {i:2d}: (vazio)")
        
        print("\n" + "="*60)
        print("ESTATÍSTICAS")
        print("="*60)
        print(f"Tamanho da tabela: {self.tamanho}")
        print(f"Total de registros: {self.total_registros}")
        print(f"Total de colisões: {self.colisoes}")
        print(f"Taxa de ocupação: {(self.total_registros/self.tamanho)*100:.2f}%")
        if self.total_registros > 0:
            eficiencia = ((self.total_registros - self.colisoes)/self.total_registros)*100
            print(f"Eficiência: {eficiencia:.2f}% (sem colisões)")
        else:
            print("Eficiência: 100% (sem registros)")
        print("="*60)

    
    def gerar_dados_teste(self):           
        nomes = [                          
            "João Silva", "Maria Santos", "Pedro Oliveira", "Ana Costa", "Carlos Ferreira",
            "Lucia Rodrigues", "Roberto Almeida", "Fernanda Lima", "Ricardo Pereira", "Juliana Souza",
            "Marcos Barbosa", "Patricia Gomes", "Andre Martins", "Camila Ribeiro", "Felipe Cardoso",
            "Vanessa Dias", "Thiago Moreira", "Renata Carvalho", "Diego Santos", "Amanda Silva",
            "Gabriel Costa", "Carolina Oliveira", "Lucas Ferreira", "Isabela Lima", "Matheus Pereira",
            "Valentina Souza", "Leonardo Barbosa", "Sophia Gomes", "Enzo Martins", "Helena Ribeiro"
        ]
        
        cpfs = [                          
            12345678901, 23456789012, 34567890123, 45678901234, 56789012345,
            67890123456, 78901234567, 89012345678, 90123456789, 12345678910,
            23456789011, 34567890122, 45678901233, 56789012344, 67890123455,
            78901234566, 89012345677, 90123456788, 12345678909, 23456789010,
            34567890121, 45678901232, 56789012343, 67890123454, 78901234565,
            89012345676, 90123456787, 12345678908, 23456789009, 34567890120
        ]
        
        idades = [25, 30, 35, 28, 42, 33, 27, 39, 31, 26, 38, 29, 36, 24, 41, 32, 37, 28, 34, 29, 40, 26, 33, 31, 35, 27, 39, 30, 36, 28]  # Lista de idades
        
        print("Gerando dados de teste...")
        for i in range(len(nomes)):        # Loop para criar pessoas de teste
            pessoa = Pessoa(str(cpfs[i]), nomes[i], idades[i])  # Cria objeto Pessoa

            self.inserir(pessoa)            # Insere na tabela hash
        
        print(f"\nDados de teste inseridos com sucesso!")
