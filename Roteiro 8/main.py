from grafo import Grafo




grafoDoGoogle = Grafo(["A","B","C","D","E","F","G"],{'A-B': 1,'A-C':4,'B-F': 2,'C-G':2,'G-F':1,'F-E':2,'D-E':3,'D-G':4})
exemploProfessor1 = Grafo(["A","B","C","D","E","F","G"],{'A-G': 1,'A-B':5,'B-C': 4,'D-B':3,'C-G':2,'D-F':2,'F-E':2,'E-B':2,"G-F":1})
exemploProfessor2 = Grafo(["A","B","C","D","E","F"],{'A-C': 2,'A-E':3,'B-C': 5,'D-B':2,'C-D':1,'B-F':3,'F-E':7,'E-D':4})



grafoDoGoogle.algoritimo_de_PRIM()
exemploProfessor1.algoritimo_de_PRIM()
exemploProfessor2.algoritimo_de_PRIM()