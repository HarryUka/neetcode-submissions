class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows , cols = len(grid) , len(grid[0])

        islands_count = 0 

        def get_count(row,col):
            if (min(row,col) < 0 or row == rows or col == cols or grid[row][col] == "0"):
                return 
            count = 1 
            grid[row][col] = "0"

            get_count(row + 1,col)
            get_count(row - 1,col)
            get_count(row,col + 1)
            get_count(row,col - 1)
            return count 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands_count += get_count(row,col)
        return islands_count  

        