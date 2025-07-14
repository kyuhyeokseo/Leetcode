class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        if m > n:
            m, n = n, m
        
        # Declare m <= n
        
        A,B = 1, m*n
        while True:
            target = (A+B) // 2
            s_cnt = 0
            t_cnt = 0

            for i in range(1, m+1):
                s_cnt += min(n, (target-1)//i)
                t_cnt += min(n, target//i)
            
            #print(target, s_cnt, t_cnt, A, B)
            if s_cnt < k and k <= t_cnt:
                return target
            elif k <= s_cnt:
                B = target-1
            else:
                A = target+1
    


