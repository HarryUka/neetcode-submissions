class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = collections.defaultdict(int)

        for num in nums:
            dic[num] += 1 

        output = []

        for num in sorted(dic, key=lambda  x : dic[x] , reverse=True):
            output.append(num)
            if len(output) >= k:
                return output 
        return output 
            

        


        
        
