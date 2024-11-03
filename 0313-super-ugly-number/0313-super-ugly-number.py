import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        if n == 1 :
            return 1
        
        cnt = 1
        
        q = []
        for p in primes :
            heapq.heappush(q, p)
        
        cnt = 1
        
        while cnt < n :
            
            N = heapq.heappop(q)
            ret = N
            
            for p in primes[::-1]:
                
                heapq.heappush(q, N*p)
                if N % p == 0 :
                    break
            
            cnt += 1
            
        return ret
        
        
        
        
        