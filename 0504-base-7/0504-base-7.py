class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if num == 0 :
            return "0"

        sign = ''
        if num < 0:
            sign += '-'
            num *= -1
        
        val = ''
        while num > 0:
            val = str(num%7) + val
            num = num // 7
        
        ret = sign + val
        return ret