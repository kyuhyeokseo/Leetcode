class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        ret = 0

        D = {}
        for n in nums:
            if n in D:
                D[n] += 1
            else :
                D[n] = 1
        
        for n in nums:
            if n+1 in D:
                ret = max(D[n+1] + D[n], ret)
        
        return ret
                


        