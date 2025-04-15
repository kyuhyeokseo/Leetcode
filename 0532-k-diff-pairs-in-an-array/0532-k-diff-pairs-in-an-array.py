class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if len(nums) < 2 :
            return 0
        
        D = {}
        for n in nums:
            if n in D:
                D[n] += 1
            else :
                D[n] = 1
        
        #print(D)

        cnt = 0
        if k != 0:
            for key in D.keys():
                k1 = key + k
                if k1 in D:
                    cnt += 1
            return cnt
        else :
            for key in D.keys():
                if D[key] > 1:
                    cnt += 1
            return cnt
