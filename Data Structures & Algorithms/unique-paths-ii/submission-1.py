class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows , cols = len(obstacleGrid) , len(obstacleGrid[0])

        cache = {}

        def memo(r,c):
            if min(r,c) < 0  or r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0 
            
            if (r,c) in cache:
                return cache[(r,c)]
            
            if r == rows - 1 and c == cols - 1:
                return 1 
            
            cache[(r,c)] = memo(r + 1 , c) + memo(r, c + 1)

            return cache[(r,c)]

        return memo(0,0)
        