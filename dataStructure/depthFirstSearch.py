'''
*Type of Graph
1) Direct Graph
2) Undirect Graph
3) Weighted Graph (when there is cost at edge)

*Outline
1) Vertex List : all the vertex in the list
ex) vertextList = ['0','1','2','3','4','5']
2) Edge List : all the edge in the list
ex) edgeList = [(0,1),(1,0),(1,2),(1,3),(2,1),(3,1),(3,4),(4,3)]
3) Adjacency List (list in list)
ex) adjacencyList = [
    [1],
    [0,2,3],
    [1],
    [1,4],
    [5],
    [4]
]
[advantage] 
-low space complexity O(number of edge)
-traverse can be done because it is list (used in BFS, DFS)

4) Adjacency Matrix : in form of matrix, expressed edge between vertex in 0 or 1
[advantage] can know instantly whether there is edge (O(1))
[disadvantage] high space complexity O(n^2)

*Depth First Search 
1) need vertextList, edgeList, adjacency List, stack
2) return : in form of index list (in assumption that edgeList is consists of index of the node)
3) input : graphs (ex- graphs = (vertexList, edgeList)) and starting index of node

*When DFS is used?
1) determine whether there is cycle
(after DFS traverse, if there is duplicate node, there exist cycle)
2) back tracking during chess

*Python
1) adjacencyList =[[] for vertex in vertexList]
: [] as number of vertex in vertexList -> [[], [], [], [], [], [], []]
cf) [vertex for vertex in vertexList] -> ['0', '1', '2', '3', '4', '5', '6']
2) for edge in edgeList:
     adjacencyList[edge[0]].append(edge[1])
: adjacencyList completed
'''

vertexList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

def dfs(graph,start):
    vertexList, edgeList = graph
    visitedVertex =[]
    stack=[start]
    adjacencyList =[[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    while stack:
        current=stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)

    return visitedVertex

print('dfs : ',dfs(graphs,0)) #[0, 2, 5, 4, 6, 1, 3] : in form of index list


