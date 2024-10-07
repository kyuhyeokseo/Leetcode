class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n == 0 or n == 1 or n == 2 :
            return 0
        
        cnt = 0
        check = [True for _ in range(n)]
        check[0], check[1] = False, False
        
        for num in range(2, n):
            
            if check[num] :
                
                cnt += 1
                for np in range(2*num, n, num) :
                    check[np] = False
            
        return cnt
        
        
        
        