class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        

        def memo(t1,t2):
            if t1 == len(text1) or t2 == len(text2):
                return 0
            
            if (t1,t2) in cache:
                return cache[(t1,t2)]
            

            move_both , move_t1 , move_t2 = 0 , 0 , 0 

            if text1[t1] == text2[t2]:
                move_both = memo(t1 + 1,t2 + 1) + 1
            
            else:

                move_t1 = memo(t1 + 1, t2)
                move_t2 = memo(t1, t2 + 1)
            
            cache[(t1,t2)] = max(move_both,max(move_t1,move_t2))

            return cache[(t1,t2)]

        return memo(0,0)

            




            

                
        