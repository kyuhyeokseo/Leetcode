class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        if L == 1 :
            return True
        VISITED = [0 for _ in range(L)]
        VISITED[0] = 1
        for idx in range(L-1):
            if VISITED[idx] != 1 :
                continue
            max_jump = nums[idx]
            for jump in range(max_jump+1):
                VISITED[idx+jump] |= 1
                if idx + jump == L-1 :
                    return True
        
        return False  