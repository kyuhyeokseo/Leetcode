class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        if L == 1 :
            return 0
        JUMP = [-1 for _ in range(L)]
        JUMP[0] = 0
        for idx in range(L-1):
            if JUMP[idx] < 0 :
                continue
            max_jump = nums[idx]
            for jump in range(max_jump+1):
                if idx + jump >= L :
                    break
                if JUMP[idx + jump] < 0:
                    JUMP[idx+jump] = JUMP[idx] + 1
                else :
                    JUMP[idx + jump] = min(JUMP[idx + jump], JUMP[idx] + 1)
        
        return JUMP[L-1]
        
        
        