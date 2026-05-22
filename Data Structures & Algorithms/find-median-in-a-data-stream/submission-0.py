import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        # Add to min Heap 
        heapq.heappush(self.minHeap, -1 * num)
        # Check for proper placing 
        if self.maxHeap and (self.maxHeap[0]) < (-1 * self.minHeap[0]):
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap,val)

        # Balance the two heap
        if (len(self.minHeap) + 1) < len(self.maxHeap):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -1 * val)
        elif (len(self.maxHeap) + 1) < len(self.minHeap):
            val = -1 * heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, val)


    def findMedian(self) -> float:
        if (len(self.minHeap)) < len(self.maxHeap):
            return self.maxHeap[0]
        elif (len(self.maxHeap)) < len(self.minHeap):
            return (-1 * self.minHeap[0])
        else:
            return ((-1 * self.minHeap[0]) + (self.maxHeap[0])) / 2
        
        