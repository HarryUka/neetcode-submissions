class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = collections.defaultdict(list)

        for word in strs:
            sign = self.getSign(word)
            output[sign].append(word)
        return list(output.values())


    def getSign(self,word):
        sign = [0] * 26

        for char in word:
            code = ord('a') - ord(char)
            sign[code] += 1
        return tuple(sign)
        


       


        