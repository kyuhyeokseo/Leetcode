class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        sum_ = 0
        i, ans = 0, L+1
        
        if sum(nums) < target:
            return 0
        
        for l in range(L):
            
            sum_ += nums[l]
            if sum_ >= target :
                ans = min(ans, l-i+1)
            while (i<l and sum_-nums[i] >= target):
                #print(i,l)
                sum_ -= nums[i]
                ans = min(ans, l-i)
                i += 1

        return ans
