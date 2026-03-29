class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, num*(-1))

        if self.maxheap and self.minheap and ((-1)*self.maxheap[0] > self.minheap[0]):
            v = heapq.heappop(self.maxheap)
            v *= -1
            heapq.heappush(self.minheap, v)
        
        if len(self.maxheap) > len(self.minheap)+1:
            v = heapq.heappop(self.maxheap)
            v *= -1
            heapq.heappush(self.minheap, v)
        
        if len(self.minheap) > len(self.maxheap)+1:
            v = heapq.heappop(self.minheap)
            v *= -1
            heapq.heappush(self.maxheap, v)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return (-1)*self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        
        return ((self.maxheap[0]*(-1))+self.minheap[0]) / 2.0
        
        