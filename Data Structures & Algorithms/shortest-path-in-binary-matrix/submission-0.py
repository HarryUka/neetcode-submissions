class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1 
        
        n = len(grid) 

        visited = set()

        queue = deque()

        queue.append((0,0))
        length = 1 
        visited.add((0,0))

        while queue:
            for _ in range(len(queue)):
                row , col = queue.popleft()
                if row == n - 1 and col == n - 1:
                    return length 
                
                neighbors = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
                for dr , dc in neighbors:
                    nr , nc = row + dr , col + dc 
                    if (min(nr,nc) < 0 or nr == n or nc == n or (nr,nc) in visited or grid[nr][nc] == 1):
                        continue 
                    queue.append((nr,nc))
                    visited.add((nr,nc))
            length += 1
        return -1 




        