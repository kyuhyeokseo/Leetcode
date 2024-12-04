class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        while len(b) > 4 :
            
            B = map(str, b[:5])
            B = int(''.join(B))
            R = B % 1140
            b = list(map(int,str(R))) + b[5:]
            
            #print(b)
        
        if len(b) == 1 :
            B = b[0]
        else :
            b = map(str, b)
            B = int(''.join(b))
            
        R = B % 1140
        if R == 0 :
            R = 1140
        
        out = 1
        a = a % 1337
        
        for _ in range(R):
            out *= a
            if out >= 1337 :
                out %= 1337
            #print(out)
        
        return out
        
        
        
        
        
        