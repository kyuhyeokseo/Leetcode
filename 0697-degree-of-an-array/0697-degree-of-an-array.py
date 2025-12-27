class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        m = -1
        D_index = {}
        D_cnt = {}
        ret = len(nums) + 1

        for i, n in enumerate(nums):
            if n not in D_index:
                D_index[n] = [i, i]
                D_cnt[n] = 1
                m = max(m, D_cnt[n])
            else:
                D_index[n][0] = i
                D_cnt[n] += 1
                m = max(m, D_cnt[n])
        
        for k, v in D_cnt.items():
            if m == v:
                ret = min(ret, D_index[k][0] - D_index[k][1])
        
        return ret + 1
            
