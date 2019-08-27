import unittest
from grafo import *

grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'],
                {'a1': 'J-C', 'a2': 'C-E', 'a3': 'C-E', 'a4': 'C-P', 'a5': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T',
                 'a9': 'T-Z'})



visitados = []
print(grafoParaiba.DFS("J", visitados))
 

  
  
  
  
  
#funcao teste
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
