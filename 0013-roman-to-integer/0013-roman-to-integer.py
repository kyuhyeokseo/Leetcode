class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = dict()
        d['I'] = 1
        d['V'] = 5
        d['X'] = 10
        d['L'] = 50
        d['C'] = 100
        d['D'] = 500
        d['M'] = 1000
        
        result = 0
        for tmp in range(len(s)):
            if tmp == len(s)-1 :
                result += d[s[tmp]]
            else :
                if d[s[tmp]] >= d[s[tmp+1]] :
                    result += d[s[tmp]]
                else :
                    result -= d[s[tmp]]
        
        return result
        
        