from grafo_adj_dir import Grafo

# Grafo da Paraíba
g_p = Grafo([], [])
for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    g_p.adicionaVertice(i)
for i in ['J-C', 'C-E', 'C-E', 'C-P', 'C-P', 'C-M', 'C-T', 'M-T', 'T-Z']:
    g_p.adicionaAresta(i)


# Grafos completos
g_c = Grafo([], [])
for i in ['J', 'C', 'E', 'P']:
    g_c.adicionaVertice(i)
for i in ['J-C', 'J-E', 'J-P', 'C-J', 'C-E', 'C-P', 'E-J', 'E-C', 'E-P', 'P-J', 'P-C', 'P-E']:
    g_c.adicionaAresta(i)



print(g_p.warshall())






print(g_c.warshall())
