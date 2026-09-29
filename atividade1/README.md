Atividade Pratica 1 - Teoria dos Grafos
UFSM - Campus Cachoeira do Sul

OBS: Em algumas situações dentro do desenvolvimento foi usado IA como forma de agilizar pequenos processos e preencher lacunas do meu conhecimento. 

Como executar:
O trabalho foi desenvolvido e resolvido no Jupyter Notebook.
Para executar e ver todos os resultados, é necessário abrir o arquivo "atividade 1.ipynb" no VS Code ou Jupyter Notebook e rodar as celulas sequencialmente.

Arquivos da entrega:
- atividade 1.ipynb: notebook contendo todo o codigo implementado, testes e respostas de cada problema.
- README.md: instruções de execução e resumo explicativo das respostas.


Respostas dos Problemas:

Problema 1: Representações e Estruturas de Dados
1. O grafo possui 10 vértices (A até J) e 11 arestas. Foram criadas as três representações no notebook: lista_adj, matriz_adj e lista_are.
2. Foram criadas funções de conversão bidirecionais entre todas as estruturas:
   - lista_adj para matriz e matriz para lista_adj
   - lista_are para matriz e matriz para lista_are
   - lista_adj para lista_are e lista_are para lista_adj
   Todas foram testadas imprimindo as saídas convertidas diretamente nas células do notebook.
3. Estacoes a no maximo 2 conexoes de distância da estacao central A:
   - 1 conexão de distância: B e C
   - 2 conexões de distância: D (via B e C) e E (via C)
   Portanto, as outras estações são: B, C, D e E.
   - Algoritmo mais direto: A Lista de Adjacência, pois acessa diretamente os vizinhos imediatos de A e, na sequência, os vizinhos desses vizinhos, sem precisar percorrer posições vazias (como os zeros da matriz) nem varrer todas as arestas do grafo repetidamente.
   - Algoritmo que leva menos tempo: A Lista de Adjacência, pois como o grafo é esparso, ela percorre estritamente o número de conexões existentes, enquanto a matriz percorre n colunas para cada linha, e a lista de arestas percorre todas as arestas a cada busca.


Problema 2: Operacoes em Grafos
- vizinhos(v): retorna a lista com os vizinhos de v. Exemplo: vizinhos de C sao A, D e E.
- grau(v): calcula o grau de v contando quantos vizinhos ele tem.
- ha_aresta(u, v): testa se existe uma aresta entre u e v, retornando True ou False.


Problema 3: Busca em Largura (BFS)
Implementada com fila (Q), inicializando visitado com falso, distancia com infinito e ant com nulo conforme o slide 33 da aula.
Respostas para o grafo a partir de A:
1. Ordem de descoberta: A -> B -> C -> D -> E -> F -> J -> G -> H -> I
2. Menor distancia de cada vertice ate A:
   d(A, A) = 0
   d(A, B) = 1
   d(A, C) = 1
   d(A, D) = 2
   d(A, E) = 2
   d(A, F) = 3
   d(A, J) = 3
   d(A, G) = 4
   d(A, H) = 5
   d(A, I) = 6
3. Antecessor de cada vertice (ant):
   A: Nenhum (Raiz)
   B: A
   C: A
   D: B
   E: C
   F: D
   J: E
   G: F
   H: G
   I: H
4. Arvore da busca em largura (9 arestas):
   [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'J'), ('F', 'G'), ('G', 'H'), ('H', 'I')]


Problema 4: Busca em Profundidade com Pilha (DFS)

Respostas para o grafo a partir de A:
1. Ordem de descoberta: A -> B -> D -> C -> E -> F -> G -> H -> I -> J
2. Arvore da busca em profundidade (9 arestas):
   [('A', 'B'), ('B', 'D'), ('D', 'C'), ('C', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'H'), ('H', 'I'), ('E', 'J')]
3. Comparacao entre a Arvore da BFS e a da DFS:
   - Diferencas em termos de Niveis (Profundidade/Altura):
     A arvore da BFS e mais larga e rasa, possuindo 7 niveis (nivel 0 a 6). Na BFS, o nivel do vertice na arvore corresponde exatamente ao menor caminho (menor numero de arestas) a partir de A.
     A arvore da DFS e mais estreita e profunda, possuindo 9 niveis (nivel 0 a 8). Na DFS, os caminhos sao explorados ate o fim antes do backtracking. Por isso, vertices como C (que e vizinho direto de A e fica no nivel 1 da BFS) ficam no nivel 3 na DFS atraves do caminho A -> B -> D -> C.
   - Diferencas em termos de Grau dos Vertices na Arvore:
     No grafo original os vertices C, D, E, F tem grau 3; A, B, G, H tem grau 2; I, J tem grau 1.
     Na BFS, a raiz A tem grau 2 (gera dois ramos imediatos: B e C). Na DFS, a raiz A tem grau 1 (inicia um caminho unico linear atraves de B).
     Na DFS, o vertice E atua como uma bifurcacao profunda, mantendo grau 3 (conectado ao pai C e aos filhos F e J), enquanto na BFS as ramificacoes sao distribuidas horizontalmente e nenhum vertice tem grau 3 na arvore geradora.
