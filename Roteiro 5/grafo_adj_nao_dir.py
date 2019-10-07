# -*- coding: utf-8 -*-

class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append('-')
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

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

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def vertices_nao_adjacentes(self):
        resultado = []
        verticies = self.N
        for i in range(len(self.M)):
            for j in range(i, len(self.M[i])):
                if int(self.M[i][j]) == 0:
                     resultado.append(verticies[i] + self.SEPARADOR_ARESTA + verticies[j])
        return resultado


    def ha_laco(self):
        for i in range(len(self.M)):
                if int(self.M[i][i]) >= 1:
                    return True
        return False


    def ha_paralelas(self):

        for i in range(len(self.M)):
            for j in range(i, len(self.M[i])):
                if int(self.M[i][j]) > 1:
                    return True
        return False




    def grau(self, vertice):

        index = 0
        for i in range(len(self.N)):
            if self.N[i] == vertice:
                index = i
                break

        grau = 0
        for i in range(len(self.M[index])):
            if self.M[index][i] == self.SEPARADOR_ARESTA:
                grau += int(self.M[i][index])
            else:
                grau += int(self.M[index][i])

        return grau
    def arestas_sobre_vertice(self, vertice):

        vertices = self.N
        index = 0
        for i in range(len(self.N)):
            if self.N[i] == vertice:
                index = i
                break

        lista =[]
        for i in range(len(self.M[index])):
            if self.M[index][i] != self.SEPARADOR_ARESTA and self.M[index][i] > 0:
                lista.append(vertices[index]+self.SEPARADOR_ARESTA+vertices[i])
            elif self.M[index][i] == self.SEPARADOR_ARESTA and self.M[i][index] > 0:
                lista.append(vertices[i] + self.SEPARADOR_ARESTA + vertices[index])

        return lista





    def eh_completo(self):
        for i in range(len(self.M)):
            for j in range(i, len(self.M[i])):
                if int(self.M[i][j]) == 0 and j > i:
                    return False
        return True

    def caminho_euleriano(self):


        cont_impar = 0
        impares = []
        totalCaminhos = 0

        for a in range(len(self.M)):
            for b in range(len(self.M)):
                if str(self.M[a][b]).isdigit() and self.M[a][b] == 1:
                    totalCaminhos += self.M[a][b]

        for vertice in self.N:
            if self.grau(vertice) % 2 != 0:

                cont_impar += 1
                impares.append(vertice)


        if cont_impar == 0 or cont_impar == 2:
            return "Caminho Eulereano Encontrado = " + str(self.procurar_caminho_euleriano(impares,totalCaminhos))


        return False

    def procurar_caminho_euleriano(self, impares,totalCaminhos):


        if len(impares) == 2:
            analisar = impares
        else:
            analisar = self.N

        for i in analisar:
            lista = []
            listaFinal = []

            self.procurar_caminhos_internos(i,lista, listaFinal)
            #print(listaFinal)


            if totalCaminhos == len((listaFinal)):
                listaRetorno = []
                listaRetorno.append(listaFinal[0])
                cont = 1

                for j in range(1,len(listaFinal)):
                    v1,v2 = listaRetorno[j-1].split(self.SEPARADOR_ARESTA)
                    v3,v4 = listaFinal[j].split(self.SEPARADOR_ARESTA)

                    if v2 == v3:
                        listaRetorno.append(listaFinal[j])
                    else:
                        listaRetorno.append(v4+self.SEPARADOR_ARESTA+v3)

                return listaRetorno





    def procurar_caminhos_internos(self, vertice, listaArestas, listaFinal):

        index = 0
        for i in range(len(self.N)):
            if self.N[i] == vertice:
                index = i
                break

        listaLigacoes = []
        for i in range(len(self.M)):
            if str(self.M[i][index]).isdigit() and self.M[i][index] > 0 and self.N[i]+self.SEPARADOR_ARESTA+vertice not in listaArestas:
                listaLigacoes.append(self.N[i])
                for j in range(self.M[i][index]):

                    IDF = 0
                    for k in range(len(listaArestas)):
                        v1, v2 = listaArestas[k].split(self.SEPARADOR_ARESTA)
                        if v2 == vertice and len(listaArestas) != 0 and v1 != vertice:
                            IDF = k+1
                    if IDF != 0:
                        listaArestas.insert(IDF,vertice+self.SEPARADOR_ARESTA+self.N[i])
                    else:
                        listaArestas.append(vertice+self.SEPARADOR_ARESTA+self.N[i])



            if str(self.M[index][i]).isdigit() and self.M[index][i] > 0 and self.N[i]+self.SEPARADOR_ARESTA+vertice not in listaArestas:
                listaLigacoes.append(self.N[i])
                for j in range(self.M[index][i]):
                    #listaArestas.append(vertice+self.SEPARADOR_ARESTA+self.N[i])

                    IDF = 0
                    for k in range(len(listaArestas)):
                        v1, v2 = listaArestas[k].split(self.SEPARADOR_ARESTA)
                        if v2 == vertice and len(listaArestas) != 0 and v1 != vertice:
                            IDF = k + 1
                    if IDF != 0:
                        listaArestas.insert(IDF, vertice + self.SEPARADOR_ARESTA + self.N[i])
                    else:
                        listaArestas.append(vertice + self.SEPARADOR_ARESTA + self.N[i])


        #print(vertice +"=" + str(listaLigacoes))
        #print(listaArestas)

        for i in listaLigacoes:
            if vertice + self.SEPARADOR_ARESTA+i in listaArestas:
                listaFinal.append(vertice+self.SEPARADOR_ARESTA+i)
                self.procurar_caminhos_internos(i, listaArestas, listaFinal)


    def vertices_adjacentes(self, raiz):
        index = self.N.index(raiz)
        adjacentes = []
        for i in range(index+1):
            if self.M[i][index] > 0:
                adjacentes.append(self.N[i])
        for j in range(index, len(self.M)):
            if self.M[index][j] > 0:
                adjacentes.append(self.N[j])
        return adjacentes


    def visita_hamiltoniano(self, partida, raiz, ja_visitados = [], caminho = []):
        if raiz in ja_visitados:
            if raiz == partida:
                if len(caminho)  == len(self.N):
                    return True
            return False
        adjacentes = self.vertices_adjacentes(raiz)

        ja_visitados.append(raiz)
        caminho.append(raiz)
        fechou = False
        for v in adjacentes:
            fechou = self.visita_hamiltoniano(partida,v,ja_visitados,caminho)
            if fechou == True or type(fechou)!= bool:
                return caminho
        ja_visitados.remove(raiz)
        caminho.pop()
        return False

    def padroniza_caminho(self,vertices = []):
        caminho = []
        for i in range(len(vertices)-1):
            caminho.append(vertices[i])
            caminho.append(vertices[i] + self.SEPARADOR_ARESTA + vertices[i+1])
        caminho.append(vertices[-1])
        return caminho

    def ciclo_hamiltoniano(self):
        ja_visitados = []
        falta_visitar = self.N.copy()
        caminho = []
        for v in self.N:
            partida = v

            ciclo = self.visita_hamiltoniano(v, v,ja_visitados,caminho)

            if type(ciclo) != bool:
                caminho = ciclo
                caminho.append(v)
                break
        if len(caminho) != 0:
            caminho_pronto= self.padroniza_caminho(caminho)
            return caminho_pronto
        return []

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str
