class Solution:
    def isNumber(self, s: str) -> bool:
        
        L = len(s)
        
        is_exp = False
        is_int_dec = False
        is_digit_bef = False
        is_digit_after = False
        cnt_dot = 0
        
        for i in range(L) :
            #print(s[i], self.is_num(s[i]))
            
            if (s[i] == '+' or s[i] == '-') :
                if i != 0 :
                    return False
            
            elif self.is_num(s[i]):
                is_int_dec = True
                
                if cnt_dot == 0 :
                    is_digit_bef = True
                else :
                    is_digit_after = True
                
            elif s[i] == '.' :
                if cnt_dot == 0 :
                    cnt_dot += 1
                    continue
                else :
                    return False
    
            elif s[i] == 'e' or s[i] == 'E':
                if is_int_dec == False :
                    return False
                is_exp = True
                break
            
            else :
                return False

        if is_int_dec == False :
            return False
            
        is_int = False
        if is_exp :
            t = s[i+1:]
            
            LL = len(t)
            
            for j in range(LL) :
                if t[j] == '+' or t[j] == '-' :
                    if j != 0 :
                        return False
                elif self.is_num(t[j]) :
                    is_int = True
                    continue
                else :
                    return False
                
            return is_int
        
        else : # int or dec
            if cnt_dot == 0 : # int
                return True
            else : # dec
                return (is_digit_bef or is_digit_after)
        
            
            
    def is_num(self, x) :
        if ord(x) >= ord('0') and ord(x) <= ord('9') :
            return True
        else :
            return False
        
        
        
        
        
        
        