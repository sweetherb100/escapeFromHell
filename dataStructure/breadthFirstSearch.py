'''
*Breadth First Search
1) need vertexList, edgeList, adjacencyList, Queue
2) return : in form of index list (in assumption that edgeList is consists of index of the node)
3) input : graphs (ex- graphs = (vertexList, edgeList) )and starting index of node

*When BFS is used?
1) Finding Shortest Path (Dijkstra algorithm)
'''

vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)

def bfs(graph, start) :
    vertexList,edgeList = graph
    visitedList = []
    queue=[start]
    adjacencyList = [[] for vertex in vertexList]
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while queue:
        current=queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs,0)) #[0, 1, 2, 3, 6, 4, 5]
