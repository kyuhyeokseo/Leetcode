class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        s = 0
        D = {}

        cnt = 0
        for n in nums:
            s += n
            
            if s == k:
                cnt += 1
            
            if s - k in D:
                cnt += D[s-k]
        
            if s in D:
                D[s] += 1
            else :
                D[s] = 1
        
        return cnt

        
        