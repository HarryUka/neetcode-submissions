
class Graph:    
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)


    def removeEdge(self, src: int, dst: int) -> bool:
        can_remove = True 
        if src not in self.adjList or dst not in self.adjList[src]:
            can_remove = False
            return can_remove
        else:
            self.adjList[src].remove(dst)
            return can_remove 


    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList:
            return False 
        visited = set()
        queue = deque()

        visited.add(src)
        queue.append(src)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True 
                for neighbor in self.adjList[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return False

