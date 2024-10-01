class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1, v2 = list(map(int, version1.split('.'))), list(map(int, version2.split('.')))
        
        L1, L2 = len(v1), len(v2)

        for i in range(max(L1, L2)) :
            if i < min(L1, L2) :
                if v1[i] > v2[i] :
                    return 1
                elif v1[i] < v2[i] :
                    return -1
            else :
                if L1 < L2 :
                    if v2[i] > 0 :
                        return -1
                elif L1 > L2 :
                    if v1[i] > 0 :
                        return 1
        
        return 0
        
        
        
        