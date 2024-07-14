class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        
        sum_ = 0
        min_ = 0
        max_ = 0
        sum_list = []
        min_list = []
        max_list = []
        
        ans1 = -99999
        tmp = 99999
        
        for i in range(len(nums)) :
            num = nums[i]
            
            min_ = min(min_, sum_)
            min_list.append(min_)
            
            sum_ += num
            sum_list.append(sum_) 
            ans1 = max(ans1, sum_ - min_)
            
        all_sum = sum_
        
            
        if len(nums) > 2 :
            new_nums = nums[1:-1]
            sum_ = 0
            
            for i in range(len(new_nums)) :
                num = new_nums[i]

                max_ = max(max_, sum_)
                max_list.append(max_)

                sum_ += num
                sum_list.append(sum_) 
                tmp = min(tmp, sum_ - max_)

            ans2 = all_sum - tmp

        
            return max(ans1, ans2)
        
        else :
            return ans1
        
        
        
        