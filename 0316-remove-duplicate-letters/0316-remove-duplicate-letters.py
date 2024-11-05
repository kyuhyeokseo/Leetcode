class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        cnt = [0] * 26
        for x in s :
            cnt[ord(x)-ord('a')] += 1
        
        U = set()
        ans = []
        
        for x in s :
            if len(ans) == 0 :
                U.add(x)
                ans.append(x)
            elif x not in U and ans[-1] < x :
                U.add(x)
                ans.append(x)
            elif x not in U and ans[-1] >= x :
                while ans and ans[-1] >= x and cnt[ord(ans[-1])-ord('a')] > 0:
                    d = ans.pop()
                    U.discard(d)
                U.add(x)
                ans.append(x)
            
            cnt[ord(x)-ord('a')] -= 1
        
        return ''.join(ans)
        
        
        
        
        