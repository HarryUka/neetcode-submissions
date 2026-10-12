class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        minHeap = []
        for stone in stones:
            minHeap.append(-stone)

        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            print(minHeap)
            y = -1 * heapq.heappop(minHeap)
            print(y)
            x = -1 * heapq.heappop(minHeap)
            print(x)

            if x == y:
                heapq.heappush(minHeap,-0)
            if x < y:
                y -= x
                heapq.heappush(minHeap,-y)
            
        return -minHeap[0]
            


        