class Solution:
    def reverseVowels(self, s: str) -> str:
        
        def aeiou(x:str ) -> bool:
            
            return x.lower() in ['a', 'e', 'i', 'o', 'u']
        
        L = len(s)
        i,j = 0, L-1
        out = list(s)
        
        while i < L and aeiou(out[i]) == False :
            i += 1
        while j > -1 and aeiou(out[j]) == False :
            j -= 1
        
        while i < j :
            out[i], out[j] = out[j], out[i]
            
            i += 1
            j -= 1
            
            while i < L and aeiou(out[i]) == False :
                i += 1
            while j > -1 and aeiou(out[j]) == False :
                j -= 1
        
        return ''.join(out)
        
        
        
        