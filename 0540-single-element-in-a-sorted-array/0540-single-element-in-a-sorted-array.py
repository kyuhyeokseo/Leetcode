class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        while len(nums) > 1:

            L = len(nums)
            I = (L+1)//4 * 2

            if nums[I-1] == nums[I-2]:
                nums = nums[I:]
                if L == 3:
                    return nums[-1]
            else:
                nums = nums[:I+1]
                if L == 3:
                    return nums[0]

        return nums[0]
