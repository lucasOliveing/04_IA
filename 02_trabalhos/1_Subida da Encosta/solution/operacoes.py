import sys
from itertools import permutations
from random import shuffle, sample
from math import sqrt


#estado inicial, ler um arquivo e devolve um Dic com pontos e cordenadas;
#a ordem dos pontos define o caminho do caixeiro viajante e, é a ordem das cordenas no arquivo.
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
    
    return cities



#dado um Dic com os pontos e as cordenadas, devolve a distancia total entre cada ponto
#seguindo a ordem dos pontos do Dic, 
def calcCust(cord):
    #aux = readCord()
    i = list (cord.keys())
    dists = {}
  
    j = 1

    for j in range(1, len(cord)):
        c1 = i[j-1]
        c2 = i[j]
     
        x = cord[c1][0] - cord[c2][0]
        y = cord[c1][1] - cord[c2][1]

        dist = sqrt((x*x) + (y*y))
        dists[c1, c2] = dist

    
    c1 = i[j]
    c2 = i[0]

    x = cord[c1][0] - cord[c2][0]
    y = cord[c1][1] - cord[c2][1]

    dists[c1, c2] = (sqrt ((x*x) + (y*y)))

    #print(dists)

    sun = 0

    for path in dists:
        sun += dists[path]
    

    #print(f"custo total = {sun:.3f}")
    return sun

#estado inicial 2, em que as entradas dos do arquivo são permutadas;
#retorna um Dic com pontos com cordenadas permutados.
def initial_2(fileName = ''):
    aux = initial_1(fileName)
    keys = list(aux.keys())
    
    keys = sample(keys, len(keys))

    cities = {key: aux[key] for key in keys}
    
    #print(cities)
    return cities

#Define a operação 1 da questão, 
#Dado um Dic com pontos e cordenadas e dois pontos, troca a posição dos dois pontos no Dic.
def op_1(cities):
    keys = list (cities.keys())
    i = sample(range(len(keys)), 2)

    op = {}
    
    for j in range(len(keys)):
        if j != i[0] and j != i[1]:
            key = keys[j]
        elif j == i[0]:
            key = keys[i[1]]
        else:
            key = keys[i[0]]
        op[key] = cities[key]
    

    #print (cities)
    #print(i)
    #print(op)
    return [op,i]

    

def op_2(cities):
    keys = list  (cities.keys())
    i = sample(range(len(keys)), 2)

    #i = [0,5]

    if i[0] > i[1]:
        slic = keys[i[0]:] + keys[:i[1]+1]
        slic = slic[::-1]

        k = 0
        for j in range(i[0], len(keys)):
            keys[j] = slic[k]
            k += 1
        for j in range(i[1]+1):
            keys[j] = slic[k]
            k += 1

    else:
        slic = keys[i[0]:i[1]+1]
        k = 0
        slic = slic[::-1]


        for j in range(i[0], i[1]+1):
            keys[j] = slic[k]
            k += 1
    
    op = { key: cities[key] for key in keys}
    
    return [op,i]



def randomNeighbor_op1(cities, i, n = 30):
    keys = list (cities.keys())
    aux = cities.copy()
    
    aux.pop(keys[i[0]])
    aux.pop(keys[i[1]])
 

    auxKeys = list (aux.keys())

    op = {}
    for j in range(n):


        auxi = sample(range(len(auxKeys)), len(auxKeys))

        l = 0
        aux.clear()

        for k in range(len(keys)):
            if k != i[0] and k != i[1]:
                key = auxKeys[auxi[l]]
               
                aux[key] = cities[key]
                l += 1
            else:
                aux[keys[k]] = cities[keys[k]]
        
        op[j] = aux.copy()

    return op


def randomNeighbor_op2(cities, i, n=2):
    keys = list (cities.keys())
    
    slic = []

    if i[0] > i[1]:
        slic = keys[i[1]+1:i[0]]
    else:
        slic = keys[:i[0]] + keys[i[1]+1:]

    op = {}
    auxKeys = []


    if len(slic) < 5:
        auxKeys = list(permutations(slic))

    else:
        for _ in range(n):
            auxKeys.append(sample(slic, len(slic)))

    print('slice ->>> ', slic)
    print("\npermutaccoes  --->>", auxKeys)

    for j in range(len(auxKeys)):

        if i[0] > i[1]:
            neighb = keys[:i[1]+1] + list( auxKeys[j]) + keys[i[0]:]
        else:
            neighb = list(auxKeys[j][:i[0]]) + keys[i[0]:i[1]+1] + list(auxKeys[j][i[0]:])

        """ print(neighb)
        op[j] = {}
        for key in neighb:
            op[j][key] = cities[key] """

        op[j] = { key: cities[key] for key in neighb}

    return op

def path(cities):
    pathh = '['
    for key in cities.keys():
        pathh +=key + '->'

    pathh += next(iter(cities)) + ']'


    return pathh


#op_2(initial_1())




