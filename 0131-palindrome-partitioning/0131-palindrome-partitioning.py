class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        out = []
    
        def findPalindrome(srt, rec):
            #print(srt, rec)
            
            if srt == len(s):
                out.append(rec[:])
            
            for j in range(srt, len(s)):
                
                if s[srt:j+1] == s[srt:j+1][::-1]:
                    rec.append(s[srt:j+1])
                    findPalindrome(j+1, rec)
                    rec.pop()
                
        findPalindrome(0, [])
        
        return out
        
        
        
        
        