class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        s = set()
        for i in range(len(nums)):
            item = nums[i]
            if (nums[i] in d) :
                d[nums[i]] += 1
            else :
                d[nums[i]] = 1
            s.add(nums[i])
        MAX = 0
        MAX_ITEM = 0
        for item in list(s):
            if d[item] > MAX :
                MAX = d[item]
                MAX_ITEM = item
        
        return MAX_ITEM
        
        
        
        
        
        