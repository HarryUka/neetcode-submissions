class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque()
        rows , cols = len(grid) , len(grid[0])
        visited = set()

        queue.append((0,0))
        visited.add((0, 0))
        length = 0 

        while queue:
            for _ in range(len(queue)):
                row , col = queue.popleft()
                if row == rows - 1 and col == cols - 1:
                    return length 

                neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

                for dr , dc in neighbors:
                    nr , nc = row + dr , col + dc 
                    if (min(nr,nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == 1 or (nr,nc) in visited):
                        continue 
                    queue.append((nr,nc))
                    visited.add((nr,nc))

            length += 1
        return -1