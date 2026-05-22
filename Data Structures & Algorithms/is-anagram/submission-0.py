class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        code1 = getCode(s) 
        code2 = getCode(t)
        return code1 == code2

def getCode(string):
    dic = [0]*26

    for char in string:
        point = ord(char) - ord("a")
        dic[point] += 1
    return tuple(dic)

        