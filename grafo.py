import heapq
from collections import defaultdict
from typing import List, Tuple, Dict, Optional

class Grafo:
    
    def __init__(self, num_vertices: int):
        self.num_vertices = num_vertices
        self.adj: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
    
    def adicionar_aresta(self, u: int, v: int, peso: int):
        self.adj[u].append((v, peso))
        self.adj[v].append((u, peso))
    
    def obter_vizinhos(self, v: int) -> List[Tuple[int, int]]:
        return self.adj[v]
    
    def dijkstra(self, origem: int) -> Tuple[Dict[int, int], Dict[int, Optional[int]]]:
        dist = {v: float('inf') for v in range(self.num_vertices)}
        prev = {v: None for v in range(self.num_vertices)}
        dist[origem] = 0
        
        heap = [(0, origem)]
        visitados = set()
        
        while heap:
            d_atual, u = heapq.heappop(heap)
            
            if u in visitados:
                continue
            
            visitados.add(u)
            
            for v, peso in self.obter_vizinhos(u):
                if v not in visitados:
                    nova_dist = dist[u] + peso
                    if nova_dist < dist[v]:
                        dist[v] = nova_dist
                        prev[v] = u
                        heapq.heappush(heap, (nova_dist, v))
        
        return dist, prev
    
    def reconstruir_caminho(self, prev: Dict[int, Optional[int]], origem: int, destino: int) -> List[int]:
        if prev[destino] is None and destino != origem:
            return []
        
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = prev[atual]
        
        caminho.reverse()
        return caminho