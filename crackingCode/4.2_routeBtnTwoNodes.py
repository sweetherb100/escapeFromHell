'''
*Question :
Given a directed graph, design an algorithm to find out whether there is route between two nodes

*Idea : 
1) use BFS (queue)
'''

vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs =(vertexList, edgeList)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    queue = [start]
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

# print(bfs(graphs,0)) #[0, 1, 2, 3, 6, 4, 5] : in form of index list
# print(bfs(graphs,3))  #[3, 4, 5]. There is no route between 3th index and 0th index

def Solution(start,end):
    traverseList = bfs(graphs,start)
    for vertex in traverseList:
        if vertex == end :
            return True
    return False

print(Solution(0,3)) #True
print(Solution(3,0)) #False



