import unittest
from grafo import *

grafoBonitinho = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G','Z','H','X'],
                {'a1': 'A-B', 'a2': 'B-G', 'a3': 'G-H', 'a4': 'B-C', 'a5': 'C-D', 'a6': 'D-E', 'a7': 'E-F', 'a8': 'F-A', 'a9':'X-Z'})




analizados = []
print(grafoBonitinho.ha_caminho('E','D',analizados))



