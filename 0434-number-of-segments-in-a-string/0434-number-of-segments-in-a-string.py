class Solution:
    def countSegments(self, s: str) -> int:
        
        s = s.strip()
        a = s.split(' ')
        
        l = 0
        for item in a :
            if len(item.strip()) != 0 :
                l += 1
        return l
