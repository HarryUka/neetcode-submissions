class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        

        def getSign(inputStr):
            index = [0]*26
            
            for char in inputStr:
                pos = ord('a') - ord(char)
                index[pos] += 1
            return tuple(index)


        return getSign(s) == getSign(t)

        