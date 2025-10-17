from simulação import Simulacao

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_entrada> [arquivo_saida]")
        print("Exemplo: python main.py labirinto1.txt saida1.txt")
        return
    
    arquivo_entrada = sys.argv[1]
    arquivo_saida = sys.argv[2] if len(sys.argv) > 2 else "relatorio.txt"
    
    try:
        sim = Simulacao(arquivo_entrada)
        sim.executar()
        
        print("\n" + sim.gerar_relatorio())
        sim.salvar_relatorio(arquivo_saida)
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()