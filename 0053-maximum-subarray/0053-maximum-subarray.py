class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        sum_ = 0
        min_ = 0
        sum_list = []
        min_list = []
        
        ans = -99999
        
        for i in range(len(nums)) :
            num = nums[i]
            
            min_ = min(min_, sum_)
            min_list.append(min_)
            
            sum_ += num
            sum_list.append(sum_) 
            ans = max(ans, sum_ - min_)
            
        
        return ans
        