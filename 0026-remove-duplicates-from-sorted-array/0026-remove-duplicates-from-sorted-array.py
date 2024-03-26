class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        i = 1
        for l in range(L-1):
            if nums[i] != nums[i-1] :
                i += 1
                continue
            else :
                tmp = nums.pop(i)
                nums.append('_')
        return i