class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        ret = [0] * N
        stk = []

        for i in range(N):
            Ti = temperatures[i]
            while stk:
                j, Tj = stk.pop()
                if Tj >= Ti:
                    stk.append((j, Tj))
                    stk.append((i, Ti))
                    break
                else:
                    ret[j] = i-j
            stk.append((i, Ti))
        
        while stk:
            j, Tj = stk.pop()
            ret[j] = 0
        
        return ret
            

