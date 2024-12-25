from collections import defaultdict
import random

class Solution:

    def __init__(self, nums: List[int]):
        
        self.D = defaultdict(list)
        for i, n in enumerate(nums) :
            self.D[n].append(i)
        

    def pick(self, target: int) -> int:
        
        L = self.D[target]
        ret = random.randint(0, len(L)-1)
        return L[ret]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)