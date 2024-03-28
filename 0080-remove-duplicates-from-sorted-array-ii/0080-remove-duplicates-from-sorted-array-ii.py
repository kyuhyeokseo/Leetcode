class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        duplicate = 0
        idx = 1
        for _ in range(L-1):
            if nums[idx] != nums[idx-1]:
                duplicate = 0
                idx += 1
            elif (nums[idx] == nums[idx-1]) and (duplicate == 0) :
                duplicate = 1
                idx += 1
            else :
                tmp = nums.pop(idx)
                nums.append('_')
                
        return idx