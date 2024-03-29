from collections import deque

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        k = k % L
        nums[:] = nums[L-k:] + nums[:L-k]
        