import unittest
from grafo import *

grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T',
                 'a9': 'T-Z'})

grafoQuestao = Grafo(['A','B','C','D','E','F','G','H','I','J','K'],{'a1': 'A-B','   a2': 'A-G','a3': 'A-J','a4': 'K-G','a5': 'K-J','a6': 'J-G','a7': 'J-I','a8': 'I-G','a9': 'G-H','a10': 'H-F','a11': 'F-B','a12': 'B-G','a13': 'B-C','a14': 'C-D','a15': 'D-E','a16': 'D-B','a17': 'B-E',})

visitados = []
print(grafoParaiba.DFS("J", visitados))
visitados = []
print(grafoQuestao.DFS("K",visitados))

# def DFS(grafo,verticie, visitados, ):
#
#     visitados.append(verticie)
#     for a in grafoParaiba.A:
#         v1, v2 = grafoParaiba.A[a].split(grafo.SEPARADOR_ARESTA)
#         if v2 not in visitados and v1 == verticie:
#             visitados.append(a)
#             DFS(grafoParaiba,v2, visitados)
#     return visitados
#
# print(DFS(grafoParaiba,"J", visitados))
