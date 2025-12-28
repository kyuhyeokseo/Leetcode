class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        M, N = len(s1), len(s2)
        s1_sum = [0] * (M+1)
        s2_sum = [0] * (N+1)

        for m in range(M-1, -1, -1):
            s1_sum[m] = ord(s1[m]) + s1_sum[m+1]

        for n in range(N-1, -1, -1):
            s2_sum[n] = ord(s2[n]) + s2_sum[n+1]
        

        def dp(x, y, memo):
            if x==M and y==N:
                return 0
            elif x==M:
                return s2_sum[y]
            elif y==N:
                return s1_sum[x]
            
            if (x,y) not in memo:
                if s1[x] == s2[y]:
                    memo[(x,y)] = dp(x+1, y+1, memo)
                else:
                    left = dp(x+1, y, memo) + ord(s1[x])
                    right = dp(x, y+1, memo) + ord(s2[y])
                    memo[(x,y)] = min(left, right)
            return memo[(x,y)]
        
        return dp(0,0,{})