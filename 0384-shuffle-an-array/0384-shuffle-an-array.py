class Solution:

    def __init__(self, nums: List[int]):
        
        self.origin = nums
        self.out = nums[:]
        

    def reset(self) -> List[int]:
        self.out = self.origin[:]
        return self.out
        

    def shuffle(self) -> List[int]:
        
        random.shuffle(self.out)
        return self.out
        
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()