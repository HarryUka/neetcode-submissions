import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = collections.defaultdict(int)

        for num in nums:
            dic[num] += 1 

        heap  = []

        for num , count in dic.items():
            heapq.heappush(heap, (count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        output = []

        for count , num in heap:
            output.append(num)

        return output 
        






            

        


        
        
