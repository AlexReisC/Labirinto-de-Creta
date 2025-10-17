# Labirinto de Creta — Simulação Prisioneiro vs Minotauro

Desenvolvido por Alex Reis

## Breve descrição:
Projeto simula um prisioneiro tentando escapar de um labirinto enquanto um Minotauro patrulha e persegue
quando detecta o prisioneiro. O grafo do labirinto é ponderado; o prisioneiro explora vértices e gasta
tempo ao mover-se; o Minotauro usa caminhos pré-calculados (Dijkstra) para perseguir.

## Principais componentes:
- grafo.py: estrutura de grafo, Dijkstra e reconstrução de caminhos.
- prisioneiro.py: lógica de exploração do prisioneiro, histórico de visitas e tempo decorrido.
- minotauro.py: detecção, perseguição (usa distâncias e predecessores pré-calculados) e movimento.
- simulação.py: loop principal, leitura de entrada, controle de turnos, combate randômico, geração de relatório.
- main.py: ponto de entrada CLI (python main.py <arquivo_entrada> [arquivo_saida]).

Formato de entrada:
1ª linha: número de vértices
2ª linha: número de arestas
Próximas linhas: arestas (u v peso)
Linhas finais: entrada, saída, posição inicial do minotauro, percepção, tempo máximo

Saída:
Relatório resumido com resultado (escape, fome ou morte pelo Minotauro), caminho do prisioneiro,
tempos, e dados de detecção/perseguição — impresso e salvo em arquivo.

Uso rápido:
python main.py grafo.txt saida.txt

## Video Explicativo
![Labirinto de Creta - Alex Reis](https://youtu.be/8_clRi-yHIU)