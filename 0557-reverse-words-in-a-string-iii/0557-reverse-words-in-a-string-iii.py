class Solution:
    def reverseWords(self, s: str) -> str:
        
        sList = s.split()
        ret = ''
        for x in sList:
            ret += x[::-1] + ' '
        ret = ret.rstrip(' ')

        return ret