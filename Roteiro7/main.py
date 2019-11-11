import sys

from grafo import *

print(sys.maxsize)



grafoDrone = Grafo(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g"],
                   {1:"A-B", 1:"A-C", 1:"A-D", 1:"B-E", 1:"B-I", 1:"C-G", 1:"D-C", 1:"D-H",1: "E-F", 1:"F-B", 1:"F-J",1: "G-F", 1:"G-J", 1:"G-K", 1:"H-G",1:"H-L", 1:"I-M",1:"J-I",1:"J-N", 1:"K-O",1:"L-P",1:"M-Q",
           1:"M-S", 1:"N-R": 1, "N-S": 1, "N-T": 1, "O-S": 1, "P-T": 1, "Q-U": 1, "R-Q": 1, "R-V": 1, "S-R": 1, "S-X": 1,
           1:"U-Y", 1:"U-Z": 1, "V-b": 1, "V-Z": 1, "V-W": 1, "W-S": 1, "X-c": 1, "X-d": 1, "Y-a": 1, "a-e": 1, "c-e": 1,
           1:"c-W", 1:"e-f": 1, "e-g": 1, "T-S": 1})



grafoDrone.dijkstra("A","Z")
