class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ret = 0
        cnt = 0
        for n in nums :
            if n == 1 :
                cnt += 1
            else :
                cnt = 0
            ret = max(ret, cnt)
        
        return ret