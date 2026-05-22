class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh = 0 
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r,c))

        time = 0

        while queue and fresh:
            for _ in range(len(queue)):
                node = queue.popleft()
                r , c = node[0] , node[1]

                for dr , dc in directions:
                    newRow  = r + dr 
                    newCol = c + dc 
                    if (newRow < 0 or newCol < 0 or newRow == rows or newCol == cols):
                        continue
                    if grid[newRow][newCol] == 1:
                        fresh -= 1
                        grid[newRow][newCol] = 2
                        queue.append((newRow,newCol))
            time += 1
        
        return time if not fresh else -1







        