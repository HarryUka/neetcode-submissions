class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        cache = {}
        rows , cols = len(obstacleGrid) , len(obstacleGrid[0])

        def memo(r,c):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]

            if r == rows - 1 and c == cols - 1:
                return 1 
            
            cache[(r,c)] = memo(r + 1,c) + memo(r,c + 1)

            return cache[(r,c)]
        return memo(0,0)

    


