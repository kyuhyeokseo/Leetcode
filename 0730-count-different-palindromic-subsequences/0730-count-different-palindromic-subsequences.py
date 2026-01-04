class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        
        MAX = 10 ** 9 + 7
        N = len(s)

        if N == 1:
            return 1
        
        @lru_cache(None)
        def dp(i,j):
            if i > j :
                return 0
            elif i == j:
                return 1

            ret = 0

            if s[i] != s[j]:
                ret = 0
                for target in ['a', 'b', 'c', 'd']:
                    left, right = s[i:j+1].find(target), s[i:j+1].rfind(target)
                    #print(f'{s[i:j+1]} - TARGET {target} | INDEX: {left, right}')
                    if left >= 0:
                        ret += 1
                    if left != right:
                        ret += (dp(i+left+1,i+right-1) + 1)
                return ret % MAX
            else:
                ret = 0
                same = s[i]
                for target in ['a', 'b', 'c', 'd']:
                    if target != same:
                        left, right = s[i:j+1].find(target), s[i:j+1].rfind(target)
                        #print(f'TARGET {target} | INDEX: {left, right}')
                        if left >= 0:
                            ret += 1
                        if left != right:
                            ret += (dp(i+left+1,i+right-1) + 1)
                    else:
                        ret += (2+dp(i+1,j-1))
                return ret % MAX
            
        return dp(0, N-1) % MAX

