class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        L = len(s)
        if numRows == 1 :
            return s
        
        result = ""
        result = result + s[::2*numRows -2]
        
        for r in range(1, numRows-1) :
            tmp1 = s[r::2*numRows -2]  
            tmp2 = s[2*numRows -2 - r :: 2*numRows -2]
            for ss in range(len(tmp1)):
                result += tmp1[ss]
                if ss <= len(tmp2) -1 :
                    result += tmp2[ss]
        
        result += s[numRows-1::2*numRows -2]
        return result
        
        
        
        
        
        