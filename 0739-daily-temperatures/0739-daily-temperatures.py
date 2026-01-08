class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        ret = [0] * N
        stk = []

        for i in range(N):
            Ti = temperatures[i]
            while stk and stk[-1][1] < Ti:
                j, Tj = stk.pop()
                ret[j] = i-j         
            stk.append((i, Ti))
        
        return ret
            

