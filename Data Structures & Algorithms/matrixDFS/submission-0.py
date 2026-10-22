class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(row,col,visited):
            rows , cols = len(grid) , len(grid[0])

            if (min(row,col) < 0 or row == rows or col == cols or (row,col) in visited or grid[row][col] == 1):
                return 0 
            
            if row == rows - 1 and col == cols - 1:
                return 1 

            visited.add((row,col))
            
            count = 0 

            count += dfs(row + 1,col,visited)
            count += dfs(row - 1,col,visited)
            count += dfs(row,col + 1,visited)
            count += dfs(row,col - 1,visited)

            visited.remove((row,col))

            return count 

        return dfs(0,0,set())
