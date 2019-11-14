from Roteiro7.grafo import Grafo

grafoTeste = Grafo(["A","B","C","D","E"],{'a1':'A-B','a2':'A-C','a3':'A-E','a4':'B-D','a5':'D-C','a6':'E-D','a7':'E-C'})


print(grafoTeste.dijkstra("A","C"))
