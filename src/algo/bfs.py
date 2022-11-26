import queue
import matplotlib.pyplot as plt 
from collections import defaultdict 
from queue import PriorityQueue, Queue
from matplotlib.animation import FuncAnimation  

def getHeuristics():
    ''' read heuristics.txt (cites, heuristics_distance)file'''
    _dict = dict()
    file = open('data/heuristics.txt')
    for row in file.readlines():
        if len(row.strip()) != 0:
            # in case there is another lines in the end of files (due to tying error)
            city, h_dist = row.split()
            _dict[city] = int(h_dist) 
    file.close()
    return _dict

def getCityCoordinates():
    ''' get cities files create 2 dicts 
        city = {citisCode: citi 's name}
        citiesCode  = {citi's name: [val1, val2]}
    '''
    city = {}
    citiesCode = {}
    f = open("data/cities.txt")
    j = 1 
    for i in f.readlines():
        node_city_val = i.split()
        city[node_city_val[0]] = [int(node_city_val[1]), int(node_city_val[2])]

        citiesCode[j] = node_city_val[0]
        j += 1
    return city, citiesCode

def createGraph():
# build graph from citiesGraph.txt file 
    graph = defaultdict(dict)
    file = open('data/citiesGraph.txt')
    for row in file.readlines():
        if len(row.strip()) != 0:
            city, aj, dist = row.split()
            graph[city][aj] = int(dist)
            graph[aj][city] = int(dist)
    file.close()
    return graph

def gbfs(startNode, heu, graph, goalNode):
    '''
    heu = {city, crows flies distance, ...}
    
    '''
    mainQueue = Queue()
    mainQueue.put(startNode)
    path = [startNode]
    totalDist = 0

    while not mainQueue.empty():
        currentNode = mainQueue.get()
        if currentNode==goalNode:
            break 

        adjacencies = graph[currentNode]
        tempPQ = PriorityQueue()

        for adjKey, adjRealDist in adjacencies.items():
            if adjKey not in path:
                tempPQ.put((heu[adjKey], adjKey))

        adjHeuDistance, adjKey = tempPQ.get()
        path.append(adjKey)
        totalDist += graph[currentNode][adjKey]
        mainQueue.put(adjKey)
    return path, totalDist

def Astar(startNode, heu, graph, goalNode):
    mainQueue = Queue()
    mainQueue.put(startNode)
    path = [startNode]
    totalDist = 0

    while not mainQueue.empty():
        currentNode = mainQueue.get()
        if currentNode==goalNode:
            break 

        adjacencies = graph[currentNode]
        tempPQ = PriorityQueue()
        for adjKey, adjRealDist in adjacencies.items():
            if adjKey not in path:
                distance = int(graph[currentNode][adjKey]) + int(heu[adjKey]) + totalDist
                tempPQ.put((distance, adjKey))

                
        real_and_heu_distance, adjKey = tempPQ.get()
        path.append(adjKey)
        totalDist += graph[currentNode][adjKey]
        mainQueue.put(adjKey)

    return path, totalDist


fig, ax = plt.subplots(); 

def drawMap(city, gbfs, graph):
    for i, j in city.items():
        plt.plot(j[0], j[1], 'ro')
        plt.annotate(i, (j[0] + 5, j[1]))
        print("-----------")
        print(i)
        print(graph[i]) 
        for k, v  in graph[i].items():
            n = city[k] 
            print(n)
            plt.plot(j[0], n[0], [j[1], n[1]], 'gray')
        
    for i in range(len(gbfs)):
        try:
            first = city[gbfs[i]]
            second = city[gbfs[i+1]]
            plt.plot([first[0], second[0]], [first[1], second[1]], "green")
            
        except:
            continue

    # plt.errorbar(1, 1, label='GBFS', color='green')
    # plt.legend(loc='upper right')
    # plt.show() 



if __name__=='__main__':
    #BUILD GRAPH AND HEURISTICS 
    graph = createGraph() 
    heuristics = getHeuristics()
    city, citiesCode = getCityCoordinates()
    # FIND PATH WITH GBFS AND ASTAR: 
    gbfs_path, dist = gbfs('Arad', heuristics, graph, 'Hirsova')
    print('GBFS PATH: ', gbfs_path)
    drawMap(city, gbfs_path, graph)

    plt.show()

