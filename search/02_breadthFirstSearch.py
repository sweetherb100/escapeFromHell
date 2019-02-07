'''
*Breadth First Search
1) need vertexList, edgeList, adjacencyList, Queue
2) return : in form of index list (in assumption that edgeList is consists of index of the node)
3) input : graphs (ex- graphs = (vertexList, edgeList) )and starting index of node

*When BFS is used?
1) Finding Shortest Path (Dijkstra algorithm)
'''

vertexList = [0, 1, 2, 3, 4, 5, 6] #['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)

def bfs(graph, start) :
    vertexList,edgeList = graph

    visitedVertex = []
    queue=[start]

    adjacencyList = [[] for vertex in vertexList]
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while queue:
        current=queue.pop(0) #dequeue
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                queue.append(neighbor) #enqueue
        visitedVertex.append(current)

    return visitedVertex

print(bfs(graphs,0)) #[0, 1, 2, 3, 6, 4, 5]

'''
    while queue:
        current=queue.pop() #dequeue
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                queue.insert(0,neighbor) #enqueue
        visitedVertex.append(current)
        
    return visitedVertex
'''