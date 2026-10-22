class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows , cols = len(grid) , len(grid[0]) 

        max_area = 0

        def get_area(row,col):
            if (min(row,col) < 0 or row == rows or col == cols or grid[row][col] == 0):
                return 0 
            area = 1 
            grid[row][col] = 0 

            area += get_area(row + 1,col)
            area += get_area(row - 1,col)
            area += get_area(row,col + 1)
            area += get_area(row,col - 1)

            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area,get_area(row,col))
                else:
                    continue 
        return max_area