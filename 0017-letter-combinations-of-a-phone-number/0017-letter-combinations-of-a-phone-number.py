class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {}
        for num in range(2, 8):
            d[str(num)] = [chr(ord('a')+3*(num-2)), chr(ord('a')+3*(num-2) +1), chr(ord('a')+3*(num-2) +2)]
        d['7'].append('s')
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']
        
        ans = []
        
        if len(digits) == 0:
            return ans
        else :
            for s in d[digits[0]]:
                ans.append(s)
        
        if len(digits) == 1:
            return ans
        
        for i in range(1, len(digits)):
            tmp = []
            for cand in ans :
                for s in d[digits[i]]:
                    tmp.append(cand + s)
            ans = tmp[:]
            
            
        return ans
            
        