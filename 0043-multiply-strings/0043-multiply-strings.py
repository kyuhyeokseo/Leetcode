class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        L1, L2 = len(num1), len(num2)
        
        L = L1 + L2
        
        ans = [0 for _ in range(L)]
        
        for i in range(1, L1+1):
            for j in range(1, L2+1):
                
                ans[i+j-2] += int(num1[L1-i]) * int(num2[L2-j])
                
        for i in range(L):
            
            if i <= L-3 :
                ans[i+2] += ans[i] // 100
                ans[i] = ans[i] % 100
            
            if i <= L-2 :
                ans[i+1] += ans[i] // 10
                ans[i] = ans[i] % 10
        
        out = ''
        srt = False
        for i in range(L-1, -1, -1) :
            if srt == False and ans[i] == 0:
                continue
            else :
                srt = True
                out += str(ans[i])
                
        if len(out) == 0:
            return "0"
        
        return out
        
        
        