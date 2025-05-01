class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        N = list(str(n))
        L = len(N)

        if L == 1 :
            return -1
        
        for i in range(L-1, 0, -1):
            if N[i-1] >= N[i]:
                pass
            else :
                X = N[i-1]
                for j in range(i, L):
                    if N[j] <= N[i-1]:
                        j -= 1
                        break
                N[i-1] = N[j]
                N[j] = X

                A = sorted(N[i:])
                K = N[:i] + A[:]
                K = int(''.join(K))
                if K > (1<<31) -1:
                    return -1
                return K
        
        return -1

