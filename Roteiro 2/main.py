

import unittest
from grafo import *


grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})



arestas = []
for a in grafoParaiba[1]:
    arestas.append(grafoParaiba[1][a])
print(arestas)


visitados = []
def DFS(verticie, visitados):

    arestas = []
    for a in grafoParaiba[1]:
        arestas.append(grafoParaiba[1][a])

    visitados.append(verticie)
    for a, b in zip(arestas,grafoParaiba[1]):
        print("-"+str(b))
        if a[2] not in visitados:
            for b in arestas:
                print(b)
                visitados.append(b)
                DFS(a[2], visitados)
    return visitados

print(DFS("J", visitados))
