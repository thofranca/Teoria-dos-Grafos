from unittest import result
import heapq
import argparse

def carregar_grafo(caminho):
    vertices = set()
    arestas = {}
    vizinho = {}
    with open(caminho, 'r') as f:
        for linha in f:
            linha = linha.strip() 
            if not linha or linha.startswith('#'):
                continue

            partes = linha.split()
            if len(partes) != 3:
                raise ValueError(f'Erro na linha: {linha}. Deve conter 3 valores.')
            
            a, b, n = partes

            if a not in vizinho:
                vizinho[a] = []
            if b not in vizinho:
                vizinho[b] = []
        
            vertices.add(a)
            vertices.add(b)

            arestas[(a,b)] = int(n)
            arestas[(b,a)] = int(n)

            vizinho[a].append(b)
            vizinho[b].append(a)

    return vertices,arestas,vizinho


def prim_mst(G,arestas,vizinho, vertice_inicial=None):
    fila_heap = []
    dist = {}
    ant = {}
    visitados = set()

    for v in G:
        dist[v] = float('inf')
        ant[v] = None
    if vertice_inicial:
        v1 = vertice_inicial
    else: 
        v1 = list(G)[0]
    heapq.heappush(fila_heap, (0, v1))
    dist[v1] = 0
    ant[v1] = None

    while len(fila_heap) > 0:
        distancia, u = heapq.heappop(fila_heap)
        if u in visitados:
            continue 

        visitados.add(u)
        for v in vizinho[u]:
            if v not in visitados and arestas[(u,v)] < dist[v]:
                dist[v] = arestas[(u,v)]
                ant[v] = u
                heapq.heappush(fila_heap, (dist[v],v))

    return dist, ant

def make_set(c, v):
    c[v] = v

def find(v, c):
    if c[v] == v:
        return v
    else:
        return find(c[v], c)

def union(a, b, c):
    ra = find(a,c)
    rb = find(b,c)
    if ra != rb: 
        c[rb] = ra

def kruskal_mst(arestas,vertices):
    mst = []
    conjunto = {}
    for v in vertices:
        make_set(conjunto, v)
    
    arestas_ordenadas = sorted(arestas.items(), key=lambda item: item[1])
    for arestas, peso in arestas_ordenadas:
        a, b = arestas
        if find(a,conjunto) != find(b,conjunto):
            mst.append((arestas,peso))
            union(a,b,conjunto)
    
    return mst 

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str)
    parser.add_argument('--alg', type=str, required=True, choices=['prim', 'kruskal'])
    parser.add_argument('--start', type=str, help="Vértice inicial (Prim)")
    args = parser.parse_args()
    vertices,arestas,vizinho = carregar_grafo(args.input)
    if args.alg == 'prim':
        print(f'Algoritmo utilizado: Prim')

        print('\nArestas escolhidas:')
        dist, ant = prim_mst(vertices,arestas,vizinho, args.start)
        peso_total = 0
        if float('inf') in dist.values():
            print("\nAviso: O grafo é desconexo! A árvore gerada é de uma das componentes.")
        for v in ant:
            if ant[v] is not None:
                origem = ant[v]
                destino = v
                peso = dist[v]
                print(f"{origem} {destino} {peso}")
                peso_total += peso
                
        print(f"\nPeso total: {peso_total}")
    elif args.alg == 'kruskal':
        print(f'Algoritmo utilizado: Kruskal')

        print('\nArestas escolhidas:')
        mst = kruskal_mst(arestas,vertices)
        peso_total = 0
        for arestas, peso in mst:
            print(f"{arestas[0]} {arestas[1]} {peso}")
            peso_total += peso
        print(f"\nPeso total: {peso_total}")

        if len(mst) < len(vertices) - 1:
            print("\nAviso: O grafo é desconexo! Foram geradas múltiplas árvores separadas (uma floresta).")