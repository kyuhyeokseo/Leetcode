class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        La, Lb = len(a), len(b)

        cnt = 1
        repeat = (Lb // La)
    
        while cnt <= repeat + 2:
            if b in a * cnt:
                return cnt
            else:
                cnt += 1
        
        return -1
            