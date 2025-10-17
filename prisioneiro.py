from typing import List, Tuple, Dict, Optional, Set
from grafo import Grafo

class Prisioneiro:
    
    def __init__(self, posicao_inicial: int):
        self.posicao = posicao_inicial
        self.visitados: Set[int] = {posicao_inicial}
        self.caminho_percorrido: List[int] = [posicao_inicial]
        self.pilha_exploracao: List[int] = [posicao_inicial]
        self.tempo_decorrido = 0
    
    def explorar(self, grafo: Grafo) -> Tuple[int, int]:
        vizinhos = grafo.obter_vizinhos(self.posicao)
        
        nao_visitados = [(v, peso) for v, peso in vizinhos if v not in self.visitados]
        
        if nao_visitados:
            proximo, peso = nao_visitados[0]
            self.pilha_exploracao.append(proximo)
            return proximo, peso
        else:
            if len(self.pilha_exploracao) > 1:
                self.pilha_exploracao.pop()
                proximo = self.pilha_exploracao[-1]
                
                for v, peso in vizinhos:
                    if v == proximo:
                        return proximo, peso
                
                return proximo, 1
            else:
                return self.posicao, 0
        
    def mover(self, novo_vertice: int, peso_aresta: int):
        self.posicao = novo_vertice
        self.visitados.add(novo_vertice)
        self.caminho_percorrido.append(novo_vertice)
        self.tempo_decorrido += peso_aresta