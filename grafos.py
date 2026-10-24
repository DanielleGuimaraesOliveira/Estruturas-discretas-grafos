import random
QNT_VERTICES = 10
SEED = 137
PROBABILIDADE = 0.3


def gerar_grafo(qnt_vertices, prob, seed):
    sorteio = random.Random(seed)

    vertices = list(range(1, qnt_vertices + 1))
    arestas = []

    for vertice_um in vertices:
        for vertice_dois in range(vertice_um + 1, qnt_vertices + 1):
            if sorteio.random() < prob:
                arestas.append((vertice_um, vertice_dois))

    
    matriz_incidencia = [[0] * len(arestas) for _ in range(qnt_vertices)]

    for coluna, (vertice_um, vertice_dois) in enumerate(arestas):
        matriz_incidencia[vertice_um - 1][coluna] = 1
        matriz_incidencia[vertice_dois - 1][coluna] = 1

    return vertices, arestas, matriz_incidencia


def graus(matriz_incidencia):
    return [sum(linha) for linha in matriz_incidencia]

def conexo(arestas, matriz_incidencia):
    qnt_vertices = len(matriz_incidencia)
    visitados = [False] * qnt_vertices

    # Função auxiliar para realizar a busca em profundidade (DFS)
    def busca_profundidade(vertice):
        visitados[vertice] = True
        for coluna, valor in enumerate(matriz_incidencia[vertice]):
            if valor == 1:
                vertice_adjacente = arestas[coluna][0] if arestas[coluna][0] != (vertice + 1) else arestas[coluna][1]
                if not visitados[vertice_adjacente - 1] and matriz_incidencia[vertice_adjacente - 1][coluna] == 1:
                    print(f"Visitando vértice {vertice_adjacente} a partir do vértice {vertice + 1}")
                    busca_profundidade(vertice_adjacente - 1)

    busca_profundidade(0)

    print("Vértices visitados:", [i + 1 for i, v in enumerate(visitados) if v])
    return all(visitados)

def printa(vertices, arestas, matriz_incidencia):
    print("Número de vertices:", len(vertices))

    print("\nArestas:")
    for indice, aresta in enumerate(arestas, start=1):
        print(f"E{indice} = {aresta}")

    print("\nQuantidade de arestas:", len(arestas))

    print("\nMatriz de incidencia:")
    print("        ", end="")
    for j in range(len(arestas)):
        print(f"e{j + 1:<3}", end="  ")
    print()

    for i, linha in enumerate(matriz_incidencia):
        print(f"v{i + 0:<3}: ", end="")
        for valor in linha:
            print(f"{valor:>4}", end="  ")
        print()

    print("\nGraus dos vertices:")
    lista_graus = graus(matriz_incidencia)

    for indice, grau in enumerate(lista_graus, start=1):
        print(f"Vertice {indice}: grau {grau}")

    print("\nConexão do grafo:")
    print("Conexo:", "Sim\n" if conexo(arestas, matriz_incidencia) else "Não\n")


vertices, arestas, matriz_incidencia= gerar_grafo(QNT_VERTICES, PROBABILIDADE, SEED)

printa(vertices,arestas, matriz_incidencia)