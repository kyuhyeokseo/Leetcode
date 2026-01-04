class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        
        MAX = 10 ** 9 + 7
        N = len(s)

        if N == 1:
            return 1
        
        dp = [[0 for _ in range(N)] for _ in range(N)]

        for gap in range(0, N):
            for i in range(0, N-gap):
                j = i+gap

                #print(f'\nNow : ({i}, {j})')

                if gap == 0:
                    dp[i][j] = 1
                else:
                    if s[i] != s[j]:
                        ret = 0
                        for target in ['a', 'b', 'c', 'd']:
                            left, right = s[i:j+1].find(target), s[i:j+1].rfind(target)
                            #print(f'{s[i:j+1]} - TARGET {target} | INDEX: {left, right}')
                            if left >= 0:
                                ret += 1
                            if left != right:
                                ret += (dp[i+left+1][i+right-1] + 1)
                        dp[i][j] = (ret % MAX)
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
                                    ret += (dp[i+left+1][i+right-1] + 1)
                            else:
                                ret += (2+dp[i+1][j-1])
                        dp[i][j] = (ret % MAX)
        
        #for i in range(N):
        #    print(dp[i])
        
        return dp[0][-1]
