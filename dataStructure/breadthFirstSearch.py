# Breadth First Search (BFS)
# vertexList, edgeList, adjacencyList, Queue 필요
# BFS 언제 사용하는가?
# 1) Finding Shortest Path (Dijkstra 알고리즘)
#
# 복습
# 1) Stack (FILO) : append, pop() (맨뒤에 있는 요소 제거) 활용
# 2) Queue (FIFO) : insert(0,),pop() (맨뒤에 있는 요소 제거) 활용

vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertexList, edgeList)

def bfs(graph, start) :
    vertexList,edgeList = graph
    visitedList = []
    queue=[start]
    adjacencyList = [[] for vertext in vertexList]
    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while queue:
        current=queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0,neighbor)
        visitedList.append(current)
    return visitedList

print(bfs(graphs,0))
