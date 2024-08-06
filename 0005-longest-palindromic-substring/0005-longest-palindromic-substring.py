class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        L = len(s)
        
        if L == 1 :
            return s[0]
        elif L == 2 :
            if s[0] == s[1] :
                return s
            else :
                return s[0]
        else :
            out = s[0]
            
            odd = []
            even = []
            
            for idx in range(L-1) :
                if idx < L-2 :
                    if s[idx] == s[idx+2] :
                        odd.append([idx, idx+2])
                if s[idx] == s[idx+1] :
                    even.append([idx, idx+1])
            
            if len(even) != 0 :
                out = s[even[0][0]:even[0][1]+1]
            if len(odd) != 0 :
                out = s[odd[0][0]:odd[0][1]+1]
            
            d = 4
            
            while (len(even) != 0 or len(odd) != 0) and d<=L :
                #print(d, even, odd)
                
                if d%2 == 0 and len(even) != 0:
                    
                    tmp = []
                    for srt, end in even :
                        if srt-1>=0 and end+1<L :
                            if s[srt-1] == s[end+1] :
                                tmp.append([srt-1, end+1])
                    even = tmp.copy()
                    if len(even) != 0 :
                        out = s[even[0][0]:even[0][1]+1]
                
                elif d%2 == 1 and len(odd) != 0:
                    tmp = []
                    for srt, end in odd :
                        if srt-1>=0 and end+1<L :
                            if s[srt-1] == s[end+1] :
                                tmp.append([srt-1, end+1])
                    odd = tmp.copy()
                    if len(odd) != 0 :
                        out = s[odd[0][0]:odd[0][1]+1]
                
                #print(d, even, odd)
                d+=1
        
            return out
        
        