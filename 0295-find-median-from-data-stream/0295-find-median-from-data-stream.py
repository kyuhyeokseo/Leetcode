import heapq

class MedianFinder:

    def __init__(self):
        
        self.H1 = []
        self.H2 = []
        self.L1 = 0
        self.L2 = 0
        

    def addNum(self, num: int) -> None:
        
        if self.L1 == self.L2 :
            
            if self.L2 == 0 :
                heapq.heappush(self.H1, -num)
                self.L1 += 1
            else :
                minL2 = self.H2[0]
                if num <= minL2 :
                    heapq.heappush(self.H1, -num)
                    self.L1 += 1
                else :
                    minL2 = heapq.heappop(self.H2)
                    heapq.heappush(self.H2, num)
                    heapq.heappush(self.H1, -minL2)
                    self.L1 += 1

        else :
            maxL1 = -self.H1[0]
            if num >= maxL1 :
                heapq.heappush(self.H2, num)
                self.L2 += 1
            else :
                maxL1 = -heapq.heappop(self.H1)
                heapq.heappush(self.H1, -num)
                heapq.heappush(self.H2, maxL1)
                self.L2 += 1
      

    def findMedian(self) -> float:
        
        if self.L1 > self.L2 :
            return -self.H1[0]
        else :
            return (-self.H1[0] + self.H2[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()