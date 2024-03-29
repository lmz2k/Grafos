import sys

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def vertices_nao_adjacentes(self):
        arestas = self.A.values()
        resultado = []

        for i in self.N:
            for j in self.N:
                aresta_indo = "{}{}{}".format(i,self.SEPARADOR_ARESTA,j)
                aresta_voltando = "{}{}{}".format(j, self.SEPARADOR_ARESTA, i)
                if aresta_indo not in arestas and aresta_voltando not in arestas:
                    resultado.append(aresta_indo)
        return resultado


    def ha_laco(self):
        arestas = self.A.values()
        for i in arestas:
            v1,v2 = i.split(self.SEPARADOR_ARESTA)
            if v1 == v2:
                return True
        return False

    def ha_paralelas(self):
        arestas = list(self.A.values())

        for i in arestas:
            v1, v2 = i.split(self.SEPARADOR_ARESTA)
            if(arestas.count("{}{}{}".format(v1,self.SEPARADOR_ARESTA,v2)) > 1):
                return True

        return False

    def  grau(self, vertice):
        aresta = self.A

        cont = 0
        for i in aresta:
            V1, V2 = aresta[i].split(self.SEPARADOR_ARESTA)
            if V1 == vertice or V2 == vertice:
                    cont += 1

        return cont

    def arestas_sobre_vertice(self, vertice):
        aresta = self.A

        arestas_final = []
        for i in aresta:
            V1,V2 = aresta[i].split(self.SEPARADOR_ARESTA)
            if V1 == vertice or V2 == vertice:
                arestas_final.append(i)
        return arestas_final

    def eh_completo(self):
        arestas = list(self.A.values())

        verticies = self.N

        lista_completo = []

        if len(verticies) == 1:
            return True
        elif len(verticies) == 2:
            return True

        for i in range(len(verticies)):
            for j in range(i+1 , len(verticies)):
                    lista_completo.append("{}{}{}".format(verticies[i],self.SEPARADOR_ARESTA,verticies[j]))


        if len(lista_completo) != len(arestas):
            return False
        else:
            for i in range(len(lista_completo)):
                v1,v2 = lista_completo[i].split("-")
                if (lista_completo[i] not in arestas):
                    if "{}{}{}".format(v2,self.SEPARADOR_ARESTA, v1) not in arestas:
                        return False
                    continue

            return True


    def DFS(self, verticie, visitados):

        visitados.append(verticie)
        for a in self.A:
            v1,v2 = self.A[a].split(self.SEPARADOR_ARESTA)
            if v2 not in visitados and v1 == verticie:
                visitados.append(a)
                self.DFS(v2, visitados)

        return visitados

    # def dijkstraDrone(self, origem, destino, cargaInicial, cargaMaxima, pontosDeRecarga):
    #     print(pontosDeRecarga)
    #     vertices = self.N
    #     arestas = self.A.values()
    #
    #     beta = {}
    #     phi = {}
    #     pi = {}
    #
    #     for i in range(len(vertices)):
    #         beta[vertices[i]] = sys.maxsize
    #         phi[vertices[i]] = 0
    #         pi[vertices[i]] = 0
    #
    #     beta[origem] = 0
    #     phi[origem] = 1
    #     pi[origem] = self.SEPARADOR_ARESTA
    #
    #     w = origem
    #
    #     while (w != destino):
    #
    #         for a in arestas:
    #
    #             v1, v2 = a.split(self.SEPARADOR_ARESTA)
    #             if v1 == w:
    #                 if phi[v2] == 0 and beta[v2] > beta[w] + 1:
    #                     beta[v2] = beta[w] + 1
    #                     pi[v2] = w
    #
    #
    #
    #
    #
    #         menorBeta = sys.maxsize
    #         verticeMenorBeta = None
    #
    #
    #         for v in vertices:
    #
    #             if phi[v] == 0 and beta[v] < sys.maxsize and beta[v] < menorBeta:
    #                 verticeMenorBeta = v
    #                 menorBeta = beta[v]
    #
    #
    #         if cargaInicial == 1 and verticeMenorBeta not in pontosDeRecarga:
    #             for vR in pontosDeRecarga:
    #                 if phi[vR] == 0 :
    #                     print("oi")
    #                     verticeMenorBeta = vR
    #                     menorBeta = beta[vR]
    #
    #
    #         else:
    #             phi[verticeMenorBeta] = 1
    #             w = verticeMenorBeta
    #
    #         if verticeMenorBeta in pontosDeRecarga:
    #             print('carreguei')
    #             cargaInicial = cargaMaxima
    #         else:
    #             print('descarreguei')
    #             cargaInicial -= 1
    #
    #
    #
    #
    #
    #
    #
    #     atual = destino
    #     resultado = []
    #
    #     while atual != origem:
    #         resultado.append(atual)
    #         atual = pi[atual]
    #
    #     resultado.append(origem)
    #     return cargaInicial, resultado[::-1]
    def dijkstraDrone(self, origem, destino, cargaAtual, pontosDeRecarga):
        inicial = origem
        pontosDeRecarga.insert(0, origem)
        pontosDeRecarga.append(destino)

        possibilidades = {}

        for i in range(len(pontosDeRecarga)):

            for j in range(len(pontosDeRecarga)):
                if origem == pontosDeRecarga[j] or self.dijkstra(origem, pontosDeRecarga[j]) == False:
                    continue
                caminho = self.dijkstra(origem, pontosDeRecarga[j])[0]
                if caminho <= cargaAtual:
                    possibilidades['a'+str(i+j)] = origem + "-" + pontosDeRecarga[j]
            origem = pontosDeRecarga[i]
            if i > 0:
                cargaAtual= 5


        grafoAtual = Grafo(pontosDeRecarga,possibilidades)
        lista = grafoAtual.dijkstra( inicial, destino)

        if lista == False:
            return "Não há caminhos possíveis !!"

        caminhoFinal = []
        for i in range(len(lista[1]) - 1):
            caminhoFinal.append(self.dijkstra(lista[1][i], lista[1][i + 1])[1])

        Final = []

        for i in range(len(caminhoFinal)):
            for j in range(len(caminhoFinal[i])):
                if (caminhoFinal[i][j] not in Final):
                    Final.append(caminhoFinal[i][j])


        return Final





    def dijkstra(self, origem, destino):

        vertices = self.N
        arestas = self.A.values()

        beta = {}
        phi = {}
        pi = {}

        for i in range(len(vertices)):
            beta[vertices[i]] = sys.maxsize
            phi[vertices[i]] = 0
            pi[vertices[i]] = 0


        beta[origem] = 0
        phi[origem] = 1
        pi[origem] = self.SEPARADOR_ARESTA

        w = origem

        verificacao = 0

        while(w != destino):

            verificacao2 = 0
            for a in arestas:
                v1, v2 = a.split(self.SEPARADOR_ARESTA)
                if v1 == w:
                    if phi[v2] == 0 and beta[v2] > beta[w] + 1:
                        beta[v2] = beta[w] + 1
                        pi[v2] = w
                        verificacao2+=1

            menorBeta = sys.maxsize
            verticeMenorBeta = None
            for v in vertices:
                if phi[v] == 0 and beta[v] < sys.maxsize and beta[v] < menorBeta:
                    verticeMenorBeta = v
                    menorBeta = beta[v]

            if verificacao2 == 0 and menorBeta == sys.maxsize:
                verificacao += 1
                break

            phi[verticeMenorBeta] = 1
            w = verticeMenorBeta

        if verificacao == 1:
            return False

        atual = destino
        resultado = []


        while atual != origem:

            resultado.append(atual)
            atual = pi[atual]


        resultado.append(origem)
        return len(resultado),resultado[::-1]



















    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str































