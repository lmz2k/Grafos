import unittest
from grafo import *



# QUESTAO 1:

trueCase = Grafo(['A', 'B', 'C', 'D', 'E', 'F'],
                 {'a1': 'A-B', 'a2': 'B-C', 'a3': 'C-D', 'a4': 'D-E', 'a5': 'E-F','a6':'A-F'})

testeSimplesTrue = Grafo(['A', 'B', 'C'],{'a1': 'A-B', 'a2': 'B-C','a3':'C-A'})
testeSimplesFalse = Grafo(['A', 'B', 'C'],{'a1': 'A-B', 'a2': 'B-C'})
print(testeSimplesTrue.ha_ciclo())
print(testeSimplesFalse.ha_ciclo())



# QUESTAO 2

GRAFO1 = Grafo(['A', 'B', 'C'],{'a1': 'A-B', 'a2': 'B-C','a3':'C-A'})
GRAFO2 = Grafo(['A', 'B', 'C', 'D'],{'a1': 'A-B', 'a2': 'B-D','a3':'D-C'})

grafoParaiba = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'C-P', 'a5':'C-P', 'a6':'C-M', 'a7':'C-T', 'a8':'M-T', 'a9':'T-Z'})




print(GRAFO1.caminho(3))
print(GRAFO1.caminho(2))
print(GRAFO2.caminho(3))
print(grafoParaiba.caminho(5))
print(grafoParaiba.caminho(7))



# QUESTAO 3
trueCase = Grafo(['A', 'B', 'C', 'D', 'E', 'F'],
                {'a1': 'A-B', 'a2': 'A-C', 'a3': 'C-D', 'a4': 'C-E', 'a5': 'E-F', 'a6': 'B-F',})
falseCase = Grafo(['A', 'B', 'C', 'D', 'E', 'F'],

                {'a1': 'A-B', 'a2': 'A-E', 'a3': 'C-D', 'a5': 'E-F', 'a6': 'B-F',})


print(trueCase.conexo())
print(falseCase.conexo())



