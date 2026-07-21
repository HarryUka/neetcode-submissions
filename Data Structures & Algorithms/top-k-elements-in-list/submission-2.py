import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = Counter(nums)

        sortedfrequency = sorted(frequency, key=lambda x : frequency[x], reverse=True)

        output = []
        for num in sortedfrequency:
            output.append(num)
            if len(output) >= k:
                return output 
        return output

        






            

        


        
        
