class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        ret = 0

        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break

        nums = nums[i:]
        L = len(nums)

        if L < 3:
            return ret

        for k in range(L-1, 1, -1):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ret += (j-i)
                    j -= 1
                else:
                    i += 1
        
        return ret
                
        