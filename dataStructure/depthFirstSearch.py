# Graph 종류
# 1) Direct Graph
# 2) Undirect Graph
# 3) Weighted Graph (edge가 cost가 있을 때)
#
# 특징
# 1) Vertex List : 모든 점을 리스트에 넣은 것
# ex) vertextList = ['0','1','2','3','4','5']
# 2) Edge List : 모든 edge를 리스트에 넣은 것
# ex) edgeList = [(0,1),(1,0),(1,2),(1,3),(2,1),(3,1),(3,4),(4,3)]
# 3) Adjacency List (리스트의 리스트)
# ex) adjacencyList = [
#     [1],
#     [0,2,3],
#     [1],
#     [1,4],
#     [5],
#     [4]
# ]
# [장점] 공간복잡도가 낮다.O(number of edge)
# 리스트이기 때문에 traverse를 돌수 있다.
# -> BFS, DFS할때 활용
#
# 4) Adjacency Matrix : matrix 형태로 vertex 사이 edge를 0,1로 표현
# [장점] edge가 있는지 없는지 한번에 알수 있다.
# [단점] 공간복잡도 O(n^2)

# Depth First Search
# 특징
# 1) vertextList
# 2) edgeList
# 3) adjacency List
# 4) stack 필요
#
# DFS 어디서 사용하는가?
# 1) cycle있는지 없는지 판별할 때
# -> DFS 순회 다 끝난 후, 중복된 방문 노드가 있을 경우, cycle이 있음.
# 2) 체스를 두고 back tracking할 때

vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

def dfs(graph,start):
    vertexList, edgeList = graph
    visitedVertex =[]
    stack=[start]
    adjacencyList =[[] for vertex in vertexList]
    #그러면 vertexList 갯수만큼 [] 생긴다.
    # ex)[[], [], [], [], [], [], []]
    # cf) [vertex for vertex in vertexList]
    # -> ['0', '1', '2', '3', '4', '5', '6']

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])
    print('adjacencyList : ',adjacencyList)

    while stack:
        current=stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)

    return visitedVertex

print('dfs : ',dfs(graphs,0))


