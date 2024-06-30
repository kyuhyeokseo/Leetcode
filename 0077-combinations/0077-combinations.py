class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        cands = range(1, n+1)
        ans = [[]]
        
        for num in cands:
            
            ans_tmp = []
            
            for item in ans:
                if len(item) < k :
                    ans_tmp.append(item + [num])
                if len(item) + (n-num) >= k :
                    ans_tmp.append(item)
            
            ans = ans_tmp[:]
            
        
        return ans
        