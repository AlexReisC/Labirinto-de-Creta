import random
from typing import Tuple, Dict
from grafo import Grafo
from minotauro import Minotauro
from prisioneiro import Prisioneiro

class Simulacao:
    
    def __init__(self, arquivo_entrada: str):
        self.grafo, self.config = self.ler_entrada(arquivo_entrada)
        
        self.prisioneiro = Prisioneiro(self.config['entrada'])
        self.minotauro = Minotauro(self.config['pos_minotauro'], self.grafo)
        
        self.turno = 0
        self.resultado = None
        self.tempo_restante = self.config['tempo_maximo']
    
    def ler_entrada(self, arquivo: str) -> Tuple[Grafo, Dict]:
        with open(arquivo, 'r') as f:
            linhas = [linha.strip() for linha in f.readlines() if linha.strip()]
        
        idx = 0
        num_vertices = int(linhas[idx])
        idx += 1
        
        num_arestas = int(linhas[idx])
        idx += 1
        
        grafo = Grafo(num_vertices)
        
        for _ in range(num_arestas):
            u, v, peso = map(int, linhas[idx].split())
            grafo.adicionar_aresta(u, v, peso)
            idx += 1
        
        config = {
            'entrada': int(linhas[idx]),
            'saida': int(linhas[idx + 1]),
            'pos_minotauro': int(linhas[idx + 2]),
            'percepcao': int(linhas[idx + 3]),
            'tempo_maximo': int(linhas[idx + 4])
        }
        
        return grafo, config
    
    def combate(self) -> bool:
        return random.random() < 0.01
    
    def executar(self):
        print("=== INICIANDO SIMULAÇÃO ===\n")
        
        while True:
            self.turno += 1
            
            proximo_vertice, peso_aresta = self.prisioneiro.explorar(self.grafo)
            self.prisioneiro.mover(proximo_vertice, peso_aresta)
            
            self.tempo_restante -= peso_aresta
            
            if self.prisioneiro.posicao == self.config['saida']:
                self.resultado = 'ESCAPOU'
                break
            
            if self.tempo_restante <= 0:
                self.resultado = 'MORTO_FOME'
                break
            
            detectou = self.minotauro.detectar_prisioneiro(
                self.prisioneiro.posicao,
                self.config['percepcao'],
                self.turno
            )
            
            movimentos = self.minotauro.calcular_proximo_movimento(self.prisioneiro.posicao)
            
            for movimento in movimentos:
                self.minotauro.mover(movimento)
                
                if self.minotauro.posicao == self.prisioneiro.posicao:
                    self.minotauro.turno_alcance = self.turno
                    
                    if self.combate():
                        print(f"[Turno {self.turno}] COMBATE! Prisioneiro venceu! (1% de sorte)")
                    else:
                        self.resultado = 'MORTO_MINOTAURO'
                        break
            
            if self.resultado == 'MORTO_MINOTAURO':
                break
    
    def gerar_relatorio(self) -> str:
        relatorio = []
        relatorio.append("=" * 60)
        relatorio.append("RELATÓRIO DA SIMULAÇÃO - LABIRINTO DE CRETA")
        relatorio.append("=" * 60)
        relatorio.append("")
        
        if self.resultado == 'ESCAPOU':
            relatorio.append("✓ RESULTADO: PRISIONEIRO ESCAPOU COM SUCESSO!")
        elif self.resultado == 'MORTO_MINOTAURO':
            relatorio.append("✗ RESULTADO: PRISIONEIRO FOI ELIMINADO PELO MINOTAURO")
        elif self.resultado == 'MORTO_FOME':
            relatorio.append("✗ RESULTADO: PRISIONEIRO MORREU DE FOME")
        
        relatorio.append("")
        relatorio.append(f"Tempo restante de alimento: {max(0, self.tempo_restante)} unidades")
        relatorio.append(f"Tempo total decorrido: {self.prisioneiro.tempo_decorrido} unidades de tempo")
        relatorio.append(f"Número de turnos: {self.turno} turnos")
        relatorio.append("")
        
        relatorio.append("Caminho percorrido pelo prisioneiro:")
        relatorio.append(f"  {' -> '.join(map(str, self.prisioneiro.caminho_percorrido))}")
        relatorio.append(f"  Total de vértices visitados: {len(self.prisioneiro.visitados)}")
        relatorio.append("")
        
        if self.minotauro.turno_deteccao:
            relatorio.append(f"Detecção pelo Minotauro: Turno {self.minotauro.turno_deteccao}")
            
            if self.minotauro.turno_alcance:
                relatorio.append(f"Alcançado pelo Minotauro: Turno {self.minotauro.turno_alcance}")
            
            if self.minotauro.caminho_perseguicao:
                relatorio.append("Caminho do Minotauro durante perseguição:")
                relatorio.append(f"  {' -> '.join(map(str, self.minotauro.caminho_perseguicao))}")
        else:
            relatorio.append("O Minotauro não detectou o prisioneiro durante a simulação.")
        
        relatorio.append("")
        relatorio.append("=" * 60)
        
        return "\n".join(relatorio)
    
    def salvar_relatorio(self, arquivo_saida: str):
        relatorio = self.gerar_relatorio()
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(relatorio)
        print(f"\nRelatório salvo em: {arquivo_saida}")