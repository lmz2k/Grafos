from grafo_adj_nao_dir import *

teste = Grafo(['0', '1', '2', '3'])
teste.adiciona_aresta('2-0')
teste.adiciona_aresta('0-1')
teste.adiciona_aresta('2-1')
teste.adiciona_aresta('2-3')


g_c_e = Grafo([], [])
for i in ['A', 'B', 'C']:
    g_c_e.adiciona_vertice(i)
for i in ['A-B', 'B-C']:
    g_c_e.adiciona_aresta(i)



konigsberg = Grafo([], [])
for i in ['M', 'T', 'B', 'R']:
    konigsberg.adiciona_vertice(i)
for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'B-R', 'T-R']:
    konigsberg.adiciona_aresta(i)

g_p = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p.adiciona_vertice(i)
for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    g_p.adiciona_aresta(i)



print(teste.caminho_euleriano())
print(g_c_e.caminho_euleriano())



print(konigsberg.caminho_euleriano())
print(g_p.caminho_euleriano())



