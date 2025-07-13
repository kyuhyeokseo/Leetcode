class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        candidates = list(range(1,n+1,1))

        if k == 1:
            return candidates
        
        ret = []
        cnt = 0

        while cnt < k:
            #print(candidates)
            if cnt % 2 == 0:
                ret.append(candidates.pop(0))
            else:
                ret.append(candidates.pop())
            cnt += 1
            #print(ret)
        
        if cnt % 2 == 0:
            ret += candidates[::-1]
        else:
            ret += candidates[:]
        
        return ret
