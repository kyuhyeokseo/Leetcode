import heapq

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = sorted(nums, key = lambda x: str(x) * 100, reverse = True)
            
        out = ''
        for i in nums :
            out += str(i)
        return str(int(out))
            
        
        
        
        
        