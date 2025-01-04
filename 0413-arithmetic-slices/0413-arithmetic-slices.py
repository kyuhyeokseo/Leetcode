class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        L = len(nums)
        if L < 3 :
            return 0
        
        ret = 0
        curr_cnt = 0
        curr_diff = 1001

        for idx in range(1, L):
            diff = nums[idx] - nums[idx-1]

            if curr_diff == diff :
                curr_cnt += 1
            else :
                ret += int(curr_cnt * (curr_cnt+1) // 2)
                curr_cnt = 0
                curr_diff = diff

        ret += int(curr_cnt * (curr_cnt+1) // 2)

        return ret

