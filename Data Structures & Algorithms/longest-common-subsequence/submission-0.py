class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def memo(t1,t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0 
            
            if (t1,t2) in cache:
                return cache[(t1,t2)]

            same , move_right , move_left = 0,0,0
            
            if text1[t1] == text2[t2]:
                same = 1 + memo(t1 + 1, t2 + 1)
            else:
                move_right = memo(t1,t2 + 1)
                move_left = memo(t1 + 1,t2)

            cache[(t1,t2)] = max(same,max(move_right,move_left))
            return cache[(t1,t2)]
        return memo(0,0)