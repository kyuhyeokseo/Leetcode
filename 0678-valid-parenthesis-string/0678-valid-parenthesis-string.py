class Solution:
    def checkValidString(self, s: str) -> bool:
        
        upper, lower = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                upper += 1
                lower += 1
            elif s[i] == ')':
                upper -= 1
                lower -= 1
            else:
                upper += 1
                lower -= 1

            if upper < 0:
                return False

        #print(upper, lower)

        o, n = (-lower//2), (-lower%2)
        c = (upper-lower)//2 - (o+n)

        #print(o, n, c)

        val = 0
        o1 = 0
        n1 = 0

        for i in range(len(s)):
            if s[i] == '(':
                val += 1
            elif s[i] == ')':
                val -= 1
            else:
                if o1 < o:
                    o1 += 1
                    val += 1
                elif o1 == o and n1 < n:
                    n1 += 1
                else:
                    val -= 1
            
            if val < 0:
                return False
        
        return val == 0
        