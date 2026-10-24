import random
QNT_VERTICES = 10
SEED = 137
PROBABILIDADE = 0.3


def gerar_grafo(qnt_vertices, prob, sorteio):
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
    lista_graus = graus(matriz_incidencia)
    nao_nulos = [i for i, g in enumerate(lista_graus) if g > 0]

    if not nao_nulos:
        return True

    visitados = [False] * qnt_vertices

    # Função auxiliar para realizar a busca em profundidade (DFS)
    def busca_profundidade(vertice):
        visitados[vertice] = True
        for coluna, valor in enumerate(matriz_incidencia[vertice]):
            if valor == 1:
                vertice_adjacente = arestas[coluna][0] if arestas[coluna][0] != (vertice + 1) else arestas[coluna][1]
                if not visitados[vertice_adjacente - 1]:
                    busca_profundidade(vertice_adjacente - 1)

    busca_profundidade(nao_nulos[0])

    return all(visitados[i] for i in nao_nulos)

def euleriano(arestas, matriz_incidencia):
    # Critério 1: vértices de grau não nulo na mesma componente conexa
    if not conexo(arestas, matriz_incidencia):
        return False

    # Critério 2: todos os vértices de grau não nulo têm grau par
    return all(grau % 2 == 0 for grau in graus(matriz_incidencia) if grau > 0)


def sim_nao(condicao):
    return "sim" if condicao else "nao"


def printa(vertices, arestas, matriz_incidencia, prob, seed, qnt_gerados):
    lista_graus = graus(matriz_incidencia)

    print("Numero de vertices:", len(vertices))
    print(f"Probabilidade p: {prob:.2f}")
    print("Seed:", seed)
    print("\nGrafo Euleriano encontrado!")
    print("\nNumero de grafos gerados:", qnt_gerados)

    print("\nArestas:")
    print(" ".join(f"({u},{v})" for u, v in arestas))

    print("\nGraus:")
    for indice, grau in enumerate(lista_graus, start=1):
        print(f"v{indice}: {grau}")

    print("\nConexo:", sim_nao(conexo(arestas, matriz_incidencia)))
    print("Todos os graus sao pares:", sim_nao(all(grau % 2 == 0 for grau in lista_graus)))
    print("Euleriano:", sim_nao(euleriano(arestas, matriz_incidencia)))

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


# Mesmo gerador (mesma seed) para todos os grafos: cada tentativa consome a sequência seguinte
sorteio = random.Random(SEED)
qnt_gerados = 0

while True:
    vertices, arestas, matriz_incidencia = gerar_grafo(QNT_VERTICES, PROBABILIDADE, sorteio)
    qnt_gerados += 1
    if arestas and euleriano(arestas, matriz_incidencia):
        break

printa(vertices, arestas, matriz_incidencia, PROBABILIDADE, SEED, qnt_gerados)