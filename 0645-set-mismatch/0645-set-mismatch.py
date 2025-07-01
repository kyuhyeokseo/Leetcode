class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        S, X, Y = 0, 0, 0

        S = sum(nums)
        X = (len(nums) * (len(nums)+1)) // 2
        Y = sum(set(nums))
        
        return [S-Y, X-Y]
        