from math import sqrt, pow


def readFile(fileName = ''):
    if not fileName:
        fileName = 'cordenadas.txt'
    try:
        file = open(fileName, 'r')
    except:
        return "File not found"

    lines = file.readlines()

    cord = { 'x': [], 'y': []}
    temp = 'x'
    aux = ''

    for line in lines:
        for char in line:
            if char != ' ':
                aux += char
                continue
            cord[temp].append(float(aux))
            aux = ''
        cord[temp].append(float(aux))
        temp = 'y'
        aux = ''
    file.close()
    
    cities = {}
    for i in range(len(cord['x'])):
        c = chr(ord('A') + i )
        cities[c] = (cord['x'][i], cord['y'][i])
    
    # print(cities)
    return cities

def dis(cities, p1, p2):
    x1,y1 = cities[p1][0], cities[p1][1]
    x2,y2 = cities[p2][0], cities[p2][1]

    return sqrt(pow((x1 - x2),2) + pow((y1 - y2),2))


class grath:

    def __init__(self, cordenates):
        self.cordenates = cordenates
        self.grath()

    def grath(self):
        adjs = {}
        cities = self.cordenates
        keys = list(cities.keys())

        for key in keys:
            adjs[key] = {}
            for key2 in keys:
                if(key2 != key):
                    dist = round(dis(cities, key, key2),2)
                    adjs[key][key2] =  dist


        self.grafo = adjs

        def adj(cidade):
            return list(self.grafo[cidade].keys())[0]

    def ordenar(self):
        g = self.grafo
        aux = {}
        for adj in g:    
            aux[adj] = {}

            while(len(g[adj]) > 0):
                
                keys = list(g[adj].keys())
                menor = (keys[0],g[adj][keys[0]])
                # print('adj :' ,adj , menor)
                for j in range(1, len(keys)):
                    # print(keys[j], g[adj][keys[j]] ,' < ', menor[1]) 
                    if g[adj][keys[j]] < menor[1]:
                        menor = (keys[j],g[adj][keys[j]])
        
                aux[adj][menor[0]] = menor[1]
                g[adj].pop(menor[0])
        
        self.grafo = aux    

    
    def printG(self):
        for adj in self.grafo:
            print(adj,self.grafo[adj])
    
    def keys(self):
        return list(self.grafo.keys())
    
    def adjs(self, city):
        return list(self.grafo[city].keys())
    
    def adj(self, city):
        return list(self.grafo[city].keys())[0]

class AGM(grath):


    def __init__(self, cordenates):
        super().__init__(cordenates)
        self.ordenar()
    
    
    def kruskal(self, cities):

        for adj in cities:
            k = list(cities[adj].keys())[0]
            key = list(cities[k].keys())[0]

            if key != adj:
                cities[adj] = {k: cities[adj][k]}
            

            #verifica se o grafo é conexo
        while(desconexo(cities)):
            for city in cities:
                if len(cities[city]) > 1:
                    neighbor = list(cities[city].keys())[0]

                    # verifica se uma das pontas estao conectadas
                    if connected(cities, city) or connected(cities, neighbor):
                        key1 = list(cities[city].keys())[0]
                        key2 = list(cities[neighbor].keys())[0]

                        cities[city] = {key1: cities[city][key1]} #[cities[city][0]]
                        cities[neighbor] = {key2: cities[neighbor][key2]}
            
                    else:
                        #busca a menor adjacencia que esta conectada
                        key1 = ''
                        key2 = ''
                        for key1 in list(cities[city].keys())[1:]:
                            if len(cities[key1]) == 1 or connected(cities, key1):
                                break
                        for key2 in list(cities[neighbor].keys())[1:]:
                            if len(cities[key2]) == 1 or connected(cities, key2):
                                break
                        
                        if(cities[city][key1] >= cities[neighbor][key2]):
                            cities[city] = {neighbor :cities[city][neighbor]}
                            cities[neighbor] = {key2:cities[neighbor][key2]}
                        else:
                            cities[neighbor] = {city :cities[neighbor][city]}
                            cities[city] = {key1: cities[city][key1]}


        return cities
        
    def grathC(self):
        self.grafoC = {}
        for i in self.agm:
            self.grafoC[i] = self.agm[i]

            for j in self.agm:
                if i != j:
                    if i == list(self.agm[j].keys())[0]:
                        self.grafoC[i][j] = self.agm[j][i]
    
    def agm(self, caminho):
        agm = {}

        for city in self.grafo:
            if city not in caminho:
                agm[city] = {}
                for adj in self.grafo[city]:
                    if adj not in caminho:
                        agm[city][adj] = self.grafo[city][adj]

        return self.kruskal(agm)


    def agm_adj(self, city):
        return list(self.agm[city].keys())[0]
    def agm_adjs(self, city):
        return list(self.agm[city].keys())



#verifica se há alguma cidade desconectada,
#cidades desconectadas possuem a lista de adjacencias cheia, assim se a lista de adjacencia
#de uma cidade for maior q 1, essa cidade esta desconectada.
def desconexo(grafo):
    for key in grafo:
        if(len(grafo[key]) > 1):
            return True
    return False



#verifica se uma cidade é conectada, isso sigfica 
# perguntar se essa cidade é o caminha minimo de outra cidade.
def connected(cities, city):
    for key in cities:
        if len(cities[key]) == 1:
            if list(cities[key].keys())[0] == city:
                return True
    return False

# def h(state):


class state:
    def __init__(self, origem, destino,caminho = [], distancia = 0, custo = 0 ,final = False):
        self.origem = origem
        self.caminho = caminho
        self.distancia = distancia
        self.destino = destino
        self.final = final
        self.custo = custo
    
    def h(self, origem, agm):
        destino = self.destino
        percorrido = self.caminho

        n = len(percorrido)
        percorrido = percorrido + [origem ,destino]
        n += 1
        i = n
    

        n_visit = [x for x in agm.keys() if x not in percorrido]
        

        while(len(n_visit) > 0):

            adjs = agm.adjs(origem)

            for adj in adjs:
                if adj in n_visit:
                    
                    n_visit.remove(adj)
                    percorrido = percorrido[:n] + [adj] + percorrido[n:]
                    n += 1
                    origem = adj
                    break
                    
        custo = 0

        for i in range(i, len(percorrido)):
            custo += agm.grafo[percorrido[i-1]][percorrido[i]]

        return custo
    
class heap:
    def __init__(self):
        self.frontier = []
    
    def add(self, state):
        i = 0
        while(i < len(self.frontier) and self.frontier[i].custo < state.custo):
            i += 1
        self.frontier = self.frontier[:i] + [state] + self.frontier[i:]

    def remove(self):
        return self.frontier.pop(0)   
    

def a_star(origem, cordenadas):
    grafo = AGM(cordenadas)
    
    
    destino = origem

    frontier = heap()
    s = state(origem, destino, [origem])


    while(not s.final):
        adjs = grafo.adjs(s.origem)

        for adj in adjs:
            if adj not in s.caminho:
                h = s.h(adj, grafo)
                g = s.distancia + grafo.grafo[s.origem][adj]
                f = h + g

                caminho = s.caminho + [adj]
                # print('para o caminho: ', caminho ,"estimativa total: ", h, ' + ', g, ' = ', f)

                final = False
                if len(caminho) == (len(grafo.keys())): # se for verdadeiro, adiciona o destino no caminho
                    destino = adj
                    final = True
            
                frontier.add(state(adj, destino, caminho, g, f, final))
        
        s = frontier.remove()


    s.caminho = s.caminho + [origem]
    # print()
    # s.custo += grafo.grafo[destino][origem] 
                    
    print('Cidade Iniciaal: ', origem, ' | caminho = ', s.caminho, '  | Custo : ' , round(s.custo,2))




def main():

    agm = AGM(readFile())
    cordenadas = readFile()

    grafo = grath(readFile())

    for cidade in agm.keys():
        a_star(cidade, cordenadas)

    # a_star('I')
    print()
    # grafo = AGM(readFile())

    # test = grafo.agm(['A','C'])
    # print(test)
    

main()