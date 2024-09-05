class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        D = {}
        for n in nums :
            if n in D :
                D[n] += 1
            else :
                D[n] = 1
        
        out = [[]]
        
        for k in D.keys():
            
            tmp = out[:]
            for bucket in tmp :
                
                bucket_tmp = bucket[:]
                for _ in range(D[k]):
                    bucket_tmp.append(k)
                    out.append(bucket_tmp[:])
        
        return out