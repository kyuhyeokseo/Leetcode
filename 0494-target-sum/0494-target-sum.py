class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        D = {}
        D[0] = 1

        for n in nums:
            D_tmp = {}
            for key in D.keys():
                if key+n in D_tmp:
                    D_tmp[key+n] += D[key]
                else:
                    D_tmp[key+n] = D[key]
                if key-n in D_tmp:
                    D_tmp[key-n] += D[key]
                else:
                    D_tmp[key-n] = D[key]
            D = D_tmp.copy()
        
        if target in D:
            return D[target]
        else:
            return 0