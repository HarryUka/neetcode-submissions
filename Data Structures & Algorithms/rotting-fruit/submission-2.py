class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        bad_oranges = deque()
        fresh = 0

        rows , cols = len(grid) , len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    bad_oranges.append((row,col))
                elif grid[row][col] == 1:
                    fresh += 1
        if fresh == 0:
            return 0

        visited = set(bad_oranges)

        time = 0 

        while bad_oranges and fresh > 0:
            for _ in range(len(bad_oranges)):
                row , col = bad_oranges.popleft()

                neighbors = [(1,0),(0,1),(-1,0),(0,-1)]

                for dr , dc in neighbors:
                    nr , nc = dr + row , dc + col 

                    if (min(nr,nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == 2 or grid[nr][nc] == 0 or (nr,nc) in visited):
                        continue 
                    grid[nr][nc] = 2
                    fresh -= 1
                    bad_oranges.append((nr,nc))
                    visited.add((nr,nc))
            time += 1
        return time if fresh == 0 else -1