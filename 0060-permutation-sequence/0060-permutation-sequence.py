class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        k = k-1
        
        factorial_list = [1]
        
        tmp = 1
        for i in range(1, n):
            tmp = tmp * i
            factorial_list = [tmp] + factorial_list
        
        rank = 1
        rec = []
        for N in factorial_list :
            rec_tmp = k // N
            k = k%N
            rec.append(rec_tmp + 1)
        
        ans = ""
        cand = [True for _ in range(n)]
        for target in rec:
            
            cnt = 1
            
            for i in range(n):
                if cand[i] and target == cnt :
                    ans += f'{i+1}'
                    cand[i] = False
                    break
                elif cand[i] :
                    cnt += 1
            
        return ans
            
            