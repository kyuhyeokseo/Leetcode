class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse = True)
        self.top = self.nums[:k]
        self.k = k
        heapq.heapify(self.top)

    def add(self, val: int) -> int:
        if len(self.top) == self.k:
            tmp = heapq.heappop(self.top)
            if val > tmp:
                heapq.heappush(self.top, val)
                ret = heapq.heappop(self.top)
                heapq.heappush(self.top, ret)
                return ret
            else:
                heapq.heappush(self.top, tmp)
                return tmp
        else:
            heapq.heappush(self.top, val)
            ret = heapq.heappop(self.top)
            heapq.heappush(self.top, ret)
            return ret
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)