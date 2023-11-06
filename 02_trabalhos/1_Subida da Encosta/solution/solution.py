#implementacao das 8 variacoes da tecnica subida da encosta
#requer python 3.7

from operacoes import *


#Variacao 1 e 5
#Operador 1 sem randomizacao da vizinhanca
def variacao_1(actual, n = 30):

    costActual = calcCust(actual)
    status = 'INICIAL     '
    report = { 0:{'path': path(actual),'state':status, 'cost': costActual}}
    i = 0
    for i in range(1, n):
        next = op_1(actual)[0]
        costNext = calcCust(next)

        if costNext < costActual:
            actual = next
            costActual = costNext
            status = 'aceito      '
        elif costNext == costActual:
            status = 'equivalente '
        else:
            status = 'recusado    '

        report[i] = {'path': path(next), 'state': status, 'cost': costNext}

    report[i] = {'path':path(actual), 'state': 'FINAL       ', 'cost': costActual}
    

    return report


#variacao 2 e 6
#Operador 1 com randomizacao da vizinhanca
def variacao_2(actual, n = 30):

    costActual = calcCust(actual)
    status = 'INICIAL     '
    report = { 0:{'path': path(actual),'state':status, 'cost': costActual}}
    i = 0
    for i in range(1, n):
        next = op_1(actual)
        costNext = calcCust(next[0])

        neighbors = randomNeighbor_op1(next[0], next[1])

        for index in neighbors:
            neighbor = neighbors[index]
            cost = calcCust(neighbor)
            if(costNext > cost):
                next[0] = neighbor
                costNext = cost


        if costNext < costActual:
            actual = next[0]
            costActual = costNext
            status = 'aceito      '
        elif costNext == costActual:
            status = 'equivalente '
        else:
            status = 'recusado    '

        report[i] = {'path': path(next[0]) ,'state':  status, 'cost': costNext}

    report[i] = {'path':path(actual) , 'state':'FINAL       ', 'cost': costActual}
    

    return report





#Variacao 3 e 7
#Operacao 2 sem randomizacao da vizinhanca
def variacao_3(actual, n = 30):

    costActual = calcCust(actual)
    status = 'INICIAL     '
    report = { 0:{'path': path(actual),'state':status, 'cost': costActual}}
    i = 0
    for i in range(1, n):
        next = op_2(actual)[0]
        costNext = calcCust(next)

        if costNext < costActual:
            actual = next
            costActual = costNext
            status = 'aceito      '
        elif costNext == costActual:
            status = 'equivalente '
        else:
            status = 'recusado    '

        report[i] = {'path': path(next), 'state': status, 'cost': costNext}

    report[i] = {'path':path(actual), 'state':'FINAL       ', 'cost': costActual}
    

    return report


#Variacao 4 e 8
#Opereracao 2 com randomizacao da vizinhanca
def variacao_4(actual, n = 30):

    costActual = calcCust(actual)
    status = 'INICIAL     '
    report = { 0:{'path': path(actual),'state':status, 'cost': costActual}}
    i = 0
    for i in range(1, n):
        next = op_2(actual)
        costNext = calcCust(next[0])

        neighbors = randomNeighbor_op1(next[0], next[1])

        for index in neighbors:
            neighbor = neighbors[index]
            cost = calcCust(neighbor)
            if(costNext > cost):
                next[0] = neighbor
                costNext = cost


        if costNext < costActual:
            actual = next[0]
            costActual = costNext
            status = 'aceito      '
        elif costNext == costActual:
            status = 'equivalente '
        else:
            status = 'recusado    '

        report[i] = {'path': path(next[0]), 'state': status, 'cost': costNext}

    report[i] = {'path':path(actual), 'state':'FINAL       ', 'cost': costActual}
    

    return report




def main():

    fileName = 'cordenadas.txt'
    outFile = 'resultado.txt'

    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    if len(sys.argv) > 2:
        outFile = sys.argv[2]

    defaut = 'cordenadas.txt'

    try:
        ini_1 = initial_1(fileName)
        ini_2 = initial_2(fileName)
    except:
        print("Arquivo nao encontrado")
        sys.exit()

    variacao = []
    variacao.append(variacao_1(ini_1))
    variacao.append(variacao_2(ini_1))
    variacao.append(variacao_3(ini_1))
    variacao.append(variacao_4(ini_1))

    variacao.append(variacao_1(ini_2))
    variacao.append(variacao_2(ini_2))
    variacao.append(variacao_3(ini_2))
    variacao.append(variacao_4(ini_2))

    esp =int( (len(variacao[0][0]['path']) - 7)/2) + 1


    report = []

    for i in range(len(variacao)):
        report.append('')
        head = esp * " " + "Caminho" + esp* " ", '|    Status   |  Custo   |\n'
        head = ''.join(head)

        aux = int((len(head)-11)/2) *' '
        report[i] += aux + f"VARIACAO: {i+1}" + aux + '\n' 
        report[i] += head
        
        aux = len(head)
        for j in variacao[i]:
            report[i] += "-"*aux+ '\n'
            report[i] += f"{variacao[i][j]['path']} | {variacao[i][j]['state']}|  {variacao[i][j]['cost']:.3f}  |\n"
            #print("-"*aux)
            #print(variacao[i][j]['path'] + ' | ' + variacao[i][j]['state'] + '  | ', f"{variacao[i][j]['cost']:.3f}" , ' |')
        report[i] += '\n'

    for i in range(len(report)):
        print(report[i])


    outFile = open( outFile , 'w')

    char = ''


    line = 2 * esp + 36
    endLine = line
    aux = 0

    for j in range(62):
        p = aux
        for i in range(len(report)):
            for k in range(p, endLine):
                if report[i][k] != '\n':
                    outFile.write(report[i][k])
                else:
                    aux = k+1
                    break
        
        
        outFile.write('\n')
        endLine += line 


    outFile.close()





main()