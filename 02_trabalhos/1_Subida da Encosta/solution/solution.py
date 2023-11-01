import sys
import random
import math



def readCord(fileName = ''):
    if not fileName:
        fileName = 'cordenadas.txt'
    file = open(fileName, 'r')
    
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
    
    cidades = {}
    for i in range(len(cord['x'])):
        c = chr(ord('A') + i )
        cidades[c] = (cord['x'][i], cord['y'][i])

    print(cidades)

    
    return cord



def calcCust(cord):
    list = []

    for i in range(1, len(cord['x'])):
        x = cord['x'][i-1] - cord['x'][i]
        y = cord['y'][i-1] - cord['y'][i]

        dist = math.sqrt((x*x) + (y*y))
        list.append(dist)

    

    return list


cord = readCord()
distancias = calcCust(cord)

print(distancias)


