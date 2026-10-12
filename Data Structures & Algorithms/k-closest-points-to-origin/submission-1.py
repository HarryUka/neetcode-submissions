
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = []

        for point in points:
            x , y = point[0] , point[1]
            distance = (x * x) + (y * y)
            heapq.heappush(minHeap,[-distance,point])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
    
        return [res[1] for res in minHeap]


       



        