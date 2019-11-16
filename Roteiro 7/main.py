from grafo import Grafo

grafoTeste = Grafo(["A","B","C","D","E"],{'a1':'A-B','a2':'A-C','a4':'B-D','a5':'D-C','a6':'E-D','a7':'E-C'})


grafoDrone = Grafo(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7"],
                   {'a1':"A-B", 'a2':"A-C", 'a3':"A-D", 'a4':"B-H", 'a5':"B-I", 'a6':"C-F", 'a7':"D-C", 'a8':"D-E", 'a9':"H-G", 'a10':"G-B", 'a11':"G-J",
           'a12':"F-G", 'a13':"F-J", 'a14':"F-K", 'a15':"E-F", 'a16':"E-L", 'a17':"I-P", 'a18':"J-I", 'a19':"J-O", 'a20':"K-N", 'a21':"L-M", 'a22':"M-Q",
           'a23':"N-R", 'a24':"O-R", 'a25':"O-Q", 'a26':"O-5", 'a27':"P-T", 'a28':"P-R", 'a29':"T-U", 'a30':"5-T", 'a31':"5-Y", 'a32':"Q-R", 'a33':"R-5",
           'a34':"U-7", 'a35':"U-W", 'a36':"Y-W", 'a37':"Y-2", 'a38':"Y-X", 'a39':"X-R", 'a40':"R-Y", 'a41':"X-4", 'a42':"Y-1", 'a43':"Y-Z", 'a44':"1-3",
           'a45':"3-4", 'a46':"7-6", 'a47':"6-3", 'a48':"3-S"}
                   )

# print(grafoTeste.dijkstra("A","D"))
#
print("Algoritimo normal!")
print(grafoDrone.dijkstra('A','S')[1])
print("Algoritimo com pontos de recarga em: L - R - U - 6! - Carga Total!")
print(grafoDrone.dijkstraDrone('A','S',5,['L','R','U','6']))
print("Algoritimo com pontos de recarga em: L - R - U - 6! - Carga 3!")
print(grafoDrone.dijkstraDrone('A','S',3,['L','R','U','6']))


