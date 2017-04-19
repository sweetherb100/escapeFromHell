#BFS (queue)
#graph 정의

vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs =(vertexList, edgeList)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = [] #값이 들어가는게 아니고 index값이 들어간다.
    queue = [start]

    adjacencyList = [[] for vertex in vertexList] #크기 선언
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1]) #값 넣기

    while queue:
        current=queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs,0)) #[0, 1, 2, 3, 6, 4, 5] : 값은 아니고 index의 집합
print(bfs(graphs,3))  #[3, 4, 5] 즉 3th index와 0th index 사이에 route 없음


