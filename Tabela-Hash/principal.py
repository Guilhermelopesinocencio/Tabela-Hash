from TabelaHash import TabelaHash             
from Pessoa import Pessoa                     

def main():
    tabela = TabelaHash(50)                   # Inicializa tabela hash com 50 posições
    
    while True:                                
        print("\n" + "="*50)
        print("SISTEMA DE CADASTRO COM TABELA HASH")
        print("="*50)
        print("1. Inserir nova pessoa")        
        print("2. Buscar pessoa por CPF")      
        print("3. Excluir pessoa por CPF")     
        print("4. Imprimir tabela completa")   
        print("5. Gerar dados de teste (30+ registros)")  
        print("6. Sair")                      
        print("="*50)
        
        opcao = input("Escolha uma opção: ").strip()  
        
        if opcao == "1":                      
            print("\n--- INSERIR NOVA PESSOA ---")
            try:
                cpf = input("Digite o CPF: ").strip()      
                nome = input("Digite o nome: ").strip()    
                idade = int(input("Digite a idade: ").strip()) 
                
                if nome and cpf and idade > 0:              # Valida dados
                    pessoa = Pessoa(cpf, nome, idade)       # Cria objeto Pessoa
                    tabela.inserir(pessoa)                  # Insere na tabela
                else:
                    print("Dados inválidos!")
            except ValueError:                               # Se idade não for número
                print("Idade deve ser um número inteiro!")
            except Exception as e:                           # Outros erros
                print(f"Erro: {e}")
        
        elif opcao == "2":                    
            print("\n--- BUSCAR PESSOA ---")
            cpf = input("Digite o CPF para buscar: ").strip() 
            if cpf:                           # Se CPF foi informado
                pessoa = tabela.buscar(cpf)   # Busca pessoa na tabela
                if pessoa:                    # Se encontrou
                    print(f"\nPessoa encontrada: {pessoa}")
            else:
                print("CPF inválido!")
        
        elif opcao == "3":                    # Se escolheu excluir
            print("\n--- EXCLUIR PESSOA ---")
            cpf = input("Digite o CPF para excluir: ").strip() 
            if cpf:                           # Se CPF foi informado
                tabela.excluir(cpf)           # Exclui pessoa da tabela
            else:
                print("CPF inválido!")
        
        elif opcao == "4":                    
            tabela.imprimir_tabela()          # Imprime tabela completa
        
        
        elif opcao == "5":                    
            print("\n--- GERANDO DADOS DE TESTE ---")
            tabela.gerar_dados_teste()        # Gera 30+ registros de teste
        
        elif opcao == "6":                    
            print("\nSaindo do sistema...")
            break                             # Sai do loop
        
        else:                                 # Se opção inválida
            print("Opção inválida! Tente novamente.")
        
        input("\nPressione Enter para continuar...")  # Pausa para usuário

if __name__ == "__main__":                   # Se arquivo executado diretamente
    main()                                   # Chama função principal
