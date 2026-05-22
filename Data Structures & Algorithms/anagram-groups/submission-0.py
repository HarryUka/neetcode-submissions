class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = collections.defaultdict(list)


        def getSign(input):
            sign = [0] * 26

            for char in input:
                code = ord('a') - ord(char)
                sign[code] += 1
            return tuple(sign)


        for char in strs:
            code = getSign(char)
            dic[code].append(char)
        
        return list(dic.values())


        