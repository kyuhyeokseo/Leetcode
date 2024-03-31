class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = dict()
        d[1] = 'I'
        d[5] = 'V'
        d[10] = 'X'
        d[50] = 'L'
        d[100] = 'C'
        d[500] = 'D'
        d[1000] = 'M'
        
        result = ''
        target = [1000, 100, 10, 1]
        
        for idx in range(len(target)) :
            tmp = target[idx]
            
            q = num // tmp
            
            if q >= 9 :
                result = result + d[tmp] + d[tmp * 10]
                num = num % tmp
                
            elif q >= 5 :
                result = result + d[tmp * 5] + (q-5) * d[tmp]
                num = num % tmp
            
            elif q >= 4 :
                result = result + d[tmp] + d[tmp * 5]
                num = num % tmp

            elif q > 0 :
                result = result + q * d[tmp]
                num = num % tmp
            
            else :
                num = num % tmp
            
            #print(result)
            #print(num)


        return result
                
            
                
            
        
        
        
        
        
        
        
        