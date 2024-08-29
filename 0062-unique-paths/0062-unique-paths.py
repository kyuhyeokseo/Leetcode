class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        m, n = max(m-1, n-1), min(m-1, n-1)
        
        print(m,n)
        
        if n == 0 :
            return 1
        else :
            ans = 1
            m += n
            
            for i in range(n):
                ans *= m
                ans //= (i+1)
                m -= 1
            return ans
            