class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.strip()
        s += '+0'
        L = len(s)
        
        result = 0
        
        prev_op = '+'
        itmd = 1
        num = ''
        
        for i in range(L):

            if s[i] == ' ' :
                continue
                
            elif s[i].isdecimal() :
                num += s[i]
                
            elif s[i] in ['+', '-', '*', '/'] :
                
                if s[i] in ['+', '-'] :
                    if prev_op == '+' :
                        result += int(num)
                        num = ''
                    elif prev_op == '-' :
                        result -= int(num)
                        num = ''
                    elif prev_op == '*' :
                        result += int(itmd * int(num))
                        itmd = 1
                        num = ''
                    elif prev_op == '/' :
                        result += int(itmd / int(num))
                        itmd = 1
                        num = ''
                elif s[i] in ['*', '/'] :
                    if prev_op == '+' :
                        itmd = int(num)
                        num = ''
                    elif prev_op == '-' :
                        itmd = -int(num)
                        num = ''
                    elif prev_op == '*' :
                        itmd *= int(num)
                        num = ''
                    elif prev_op == '/' :
                        itmd = int(itmd / int(num))
                        num = ''
                prev_op = s[i]
            
        return result
        
        
        