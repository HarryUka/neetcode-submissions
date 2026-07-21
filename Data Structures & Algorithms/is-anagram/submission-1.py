class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def getSign(inputString):
            sign = [0] * 26
            for char in inputString:
                code = ord('a') - ord(char)
                sign[code] += 1
            return tuple(sign)



        return getSign(s) == getSign(t)

        