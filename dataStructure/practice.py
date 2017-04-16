vertexList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0,1), (0,2), (1,0) , (1,3) , (2,0) , (2,4) , (2,5) , (3,1), (4,2) , (4,6), (5,2), (6,4)]
graphs = (vertexList, edgeList)

adjacencyList =[[] for vertex in vertexList]
adjacencyList2 =[vertex for vertex in vertexList]
print(adjacencyList)
# [[], [], [], [], [], [], []]
print(adjacencyList2)
# ['0', '1', '2', '3', '4', '5', '6']

for edge in edgeList:
    print('edge[0] : ',edge[0])
    print('edge[1] : ',edge[1])
    print('************')

    # edge[0]: 0
    # edge[1]: 1
    # ** ** ** ** ** **
    # edge[0]: 0
    # edge[1]: 2
    # ** ** ** ** ** **
    # edge[0]: 1
    # edge[1]: 0
    # ** ** ** ** ** **
    # edge[0]: 1
    # edge[1]: 3
    # ** ** ** ** ** **
    # edge[0]: 2
    # edge[1]: 0
    # ** ** ** ** ** **
    # edge[0]: 2
    # edge[1]: 4
    # ** ** ** ** ** **
    # edge[0]: 2
    # edge[1]: 5
    # ** ** ** ** ** **
    # edge[0]: 3
    # edge[1]: 1
    # ** ** ** ** ** **
    # edge[0]: 4
    # edge[1]: 2
    # ** ** ** ** ** **
    # edge[0]: 4
    # edge[1]: 6
    # ** ** ** ** ** **
    # edge[0]: 5
    # edge[1]: 2
    # ** ** ** ** ** **
    # edge[0]: 6
    # edge[1]: 4
    # ** ** ** ** ** **