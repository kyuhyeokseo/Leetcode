class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        L = len(nums)
        for l in range(L):
            item = nums.pop(0)
            if item != val:
                k += 1
                nums.append(item)
        if k == L :
            return k
        else :
            for _ in range(L-k):
                nums.append('_')
            return k