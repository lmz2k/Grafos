from grafo import Grafo




grafoDoGoogle = Grafo(["A","B","C","D","E","F","G"],{'A-B': 1,'A-C':4,'B-F': 2,'C-G':2,'G-F':1,'F-E':2,'D-E':3,'D-G':4})




grafoDoGoogle.algoritimo_de_PRIM()