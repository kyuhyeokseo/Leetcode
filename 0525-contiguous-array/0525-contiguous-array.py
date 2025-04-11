class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        D = {}
        D[0] = 0

        ret = 0

        prefix = [0]
        s = 0

        for i, n in enumerate(nums):
            if n == 0:
                s -= 1
            else:
                s += 1
            prefix.append(s)

            if s not in D:
                D[s] = i+1
            else:
                ret = max(ret, i+1 - D[s])

        return ret
        


        
