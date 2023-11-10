from math import sqrt, pow

def initial_1(fileName = ''):
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
            if cities[key][0]['city'] == city:
                print("A cidade ", city, 'é a aresta minima de ', key)
                return True
    return False

def grafo(cities):
    adjs = {}
    keys = list(cities.keys())
    
    for key in keys:
        adjs[key] = []
        for key2 in keys:
            if(key2 != key):
                dist = round(dis(cities, key, key2),2)
                adjs[key].append({key2: dist, 'city':key2, 'way':dist})

        adjs[key] = sorted(adjs[key],key = lambda x: x['way'])


    for adj in adjs:
        i = adjs[adj][0]['city']
        # print(i)
        if adj != adjs[i][0]['city']:
            adjs[adj] = [adjs[adj][0]]


    for adj in adjs:
        print(adj, '->',end='{')
        for x in range(len(adjs[adj])):
            print(adjs[adj][x]['city'], end=',')
        print('}')
    #verifica se o grafo é conexo
    while(desconexo(adjs)):
        for city in adjs:
            if len(adjs[city]) > 1:
                neighbor = adjs[city][0]['city']
                print("a cidade ", city, "esta desconectada, seu visizinho mais proximo é ", neighbor)

                # verifica se uma das pontas estao conectadas
                if connected(adjs, city) or connected(adjs, neighbor):
                    if connected(adjs, city):
                        print(' a cidade ', city, 'esta conectada')
                    if connected(adjs, neighbor):
                        print(' a cidade ', neighbor, 'esta conectada')
                    adjs[city] = [adjs[city][0]]
                    adjs[neighbor] = [adjs[neighbor][0]]
                else:
                    print(city, ' e ', neighbor, ' estao desconectados')
                    i, j = 1, 1
                    for i in range(1, len(adjs[city])):
                        print('verificando se a adj ', adjs[city][i]['city'], ' da cidade ', city, 'esta conectada')
                        if len(adjs[adjs[city][i]['city']]) == 1 or connected(adjs, adjs[city][i]['city']):
                            break
                    for j in range(1, len(adjs[neighbor])):
                        print('verificando se a adj ', adjs[neighbor][j]['city'], ' da cidade ', neighbor, 'esta conectada')
                        if len(adjs[adjs[neighbor][j]['city']]) == 1 or connected(adjs, adjs[neighbor][j]['city']):
                            break
                    
                    print('A adjacencia: ',adjs[city][i]['city'], " esta conectada a ", city)
                    print('A adjacencia: ',adjs[neighbor][j]['city'], " esta conectada a ", neighbor)
                
                    if(adjs[city][i]['way'] >= adjs[neighbor][j]['way']):
                        adjs[city] = [adjs[city][0]]
                        adjs[neighbor] = [adjs[neighbor][j]]
                    else:
                        adjs[neighbor] = [adjs[neighbor][0]]
                        adjs[city] = [adjs[city][i]]



    for adj in adjs:
        for x in range(len(adjs[adj])):
            adjs[adj][x].pop('city')
            adjs[adj][x].pop('way')
        print(adj,adjs[adj])





grafo(initial_1())
