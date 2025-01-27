class Solution:
    def compress(self, chars: List[str]) -> int:
        
        rec = ''
        cnt_part = 0
        cnt = 0

        chars.append('ABCD')
        L = len(chars)

        for _ in range(L):
            c = chars.pop(0)
            
            if c != rec :
                
                cnt += cnt_part
                chars.append(rec)
                if cnt_part > 1 :
                    for t in str(cnt_part):
                        chars.append(t)
                
                cnt_part = 1
                rec = c
            
            else :
                cnt_part += 1
        
        chars.pop(0)
                
        return cnt