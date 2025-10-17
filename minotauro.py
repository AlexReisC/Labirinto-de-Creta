import random
from typing import List, Dict, Optional
from grafo import Grafo

class Minotauro:
    
    def __init__(self, posicao_inicial: int, grafo: Grafo):
        self.posicao = posicao_inicial
        self.grafo = grafo
        self.em_perseguicao = False
        self.caminho_perseguicao: List[int] = []
        self.turno_deteccao: Optional[int] = None
        self.turno_alcance: Optional[int] = None
        
        self.distancias_precalculadas: Dict[int, Dict[int, int]] = {}
        self.caminhos_precalculados: Dict[int, Dict[int, Optional[int]]] = {}
        
        for v in range(grafo.num_vertices):
            dist, prev = grafo.dijkstra(v)
            self.distancias_precalculadas[v] = dist
            self.caminhos_precalculados[v] = prev
    
    def distancia_ate(self, destino: int) -> int:
        return self.distancias_precalculadas[self.posicao][destino]
    
    def detectar_prisioneiro(self, pos_prisioneiro: int, parametro_percepcao: int, turno_atual: int) -> bool:
        distancia = self.distancia_ate(pos_prisioneiro)
        
        if distancia <= parametro_percepcao and not self.em_perseguicao:
            self.em_perseguicao = True
            self.turno_deteccao = turno_atual
            return True
        
        return self.em_perseguicao
    
    def calcular_proximo_movimento(self, pos_prisioneiro: int) -> List[int]:
        if self.em_perseguicao:
            caminho = self.grafo.reconstruir_caminho(
                self.caminhos_precalculados[self.posicao],
                self.posicao,
                pos_prisioneiro
            )
            
            if len(caminho) > 1:
                movimentos = caminho[1:min(3, len(caminho))]
                self.caminho_perseguicao.extend(movimentos)
                return movimentos
            else:
                return []
        else:
            vizinhos = self.grafo.obter_vizinhos(self.posicao)
            if vizinhos:
                proximo, _ = random.choice(vizinhos)
                return [proximo]
            else:
                return []
    
    def mover(self, destino: int):
        self.posicao = destino