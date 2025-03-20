class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        N = len(nums)
        ret = [-1] * N
        stk = []

        for i, n in enumerate(nums + nums):
            i = i % N
            if len(stk) == 0:
                stk.append((i,n))
            else:
                while stk and stk[-1][1] < n:
                    j, m = stk.pop()
                    ret[j] = n
                stk.append((i,n))

        return ret