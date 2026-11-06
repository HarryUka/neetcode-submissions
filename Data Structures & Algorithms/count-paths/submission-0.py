class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def memo(r,c):
            if r == m or c == n:
                return 0
            
            if (r,c) in cache:
                return cache[(r,c)]

            if r == m - 1 and c == n - 1:
                return 1 

            cache[(r,c)] = memo(r + 1,c) + memo(r,c + 1)

            return cache[(r,c)]

        return memo(0,0)

        
        