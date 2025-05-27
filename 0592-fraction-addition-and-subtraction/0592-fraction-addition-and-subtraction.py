import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        numers, denoms = [], []
        i, S = 0, 1
        while i < len(expression):
            
            i_numer = expression.find('/', i+1)
            numers.append(int(expression[i:i_numer]))

            i = i_numer + 1
            
            i_denom = -1
            for j in range(i, len(expression)):
                if expression[j] in ['+', '-']:
                    i_denom = j
                    break
            if i_denom == -1:
                denoms.append(int(expression[i:]))
                S *= int(expression[i:])
                i_denom = len(expression)
            else :
                denoms.append(int(expression[i:i_denom]))
                S *= int(expression[i:i_denom])
            i = i_denom

        #print(numers, denoms)

        s = 0
        for i in range(len(numers)):
            s += int(numers[i] * int(S//denoms[i]))
        
        pm = '' if s >= 0 else '-'
        s = s if s >= 0 else -s

        #print(pm, s, S)

        if s == 0:
            return '0/1'
        else :
            G = math.gcd(s, S)
            return pm + str(int(s/G)) + '/' + str(int(S/G))


