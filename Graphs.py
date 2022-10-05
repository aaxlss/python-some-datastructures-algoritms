class Graph():
    def __init__(self) -> None:
        self.nodesNumber = 0
        self.adjancenList ={}
    
    def addVertex(self,value):
        
        if value not in self.adjancenList: 
            self.adjancenList[value] = []
            self.nodesNumber += 1
            return self
        else:
            return 'This vertex already exists in the List'

    def addEdge(self,node_1, node_2):

        if node_1 not in self.adjancenList or node_2 not in self.adjancenList:
            return "one of the nodes doesn't exist"
        else:
            if node_2 in self.adjancenList[node_1]:
                return f'Connectiont to : {node_2} exist in {node_1}'
            else:
                self.adjancenList[node_1].append(node_2)

            if node_1 in self.adjancenList[node_2]:
                return f'Connectiont to : {node_1} exist in {node_2}'
            else:

                self.adjancenList[node_2].append(node_1)
        
        return self

    def showConnections(self):

        if self.nodesNumber == 0:
            return "No existing nodes"

        for node, connections in self.adjancenList.items():
            print(f'{node} ==> {connections}')
        
        return True



def main():
    graph = Graph()

    graph.addVertex(0)
    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addVertex(5)
    graph.addVertex(6)
    graph.addVertex(7)
    graph.addVertex(8)

    graph.addEdge(0,1)
    graph.addEdge(3,5)
    graph.addEdge(3,6)
    graph.addEdge(7,1)
    graph.addEdge(3,3)
    graph.addEdge(7,3)
    graph.addEdge(5,1)
    graph.addEdge(8,1)
    graph.addEdge(8,4)
    graph.addEdge(7,8)
    graph.addEdge(2,4)
    graph.addEdge(4,5)
    
    graph.showConnections()

if __name__ == '__main__':
    main()