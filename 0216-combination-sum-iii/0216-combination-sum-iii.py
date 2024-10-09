class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        if k * (k+1) / 2 > n :
            return []
        elif k * (k+1) / 2 == n :
            return [range(1,k+1)]
        
        out = []
        for level in range(k) :
            
            #print(out)
            if level == 0 :
                for m in range(1, 11-k):
                    if k * (2*m-k+1) / 2 <= n and (m + (20-k) * (k-1) / 2 ) >= n :
                        out.append([m])
            else :
                new_out = []
                extra = k-level-1
                for each in out :
                    S = sum(each)
                    for m in range(each[-1]+1, 11-k+level):
                        if (S + m + (m+1 + m+extra) * extra / 2) <= n and (S+m+ (9+9-extra+1) * extra / 2) >= n :
                            each_cpy = each[:]
                            each_cpy.append(m)
                            new_out.append(each_cpy)
                out = new_out[:]
            #print(out)
            #print('---------------')
        
        return out