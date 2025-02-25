class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        L, M, N = len(strs), m, n
        dp = [[[0 for _ in range(N+1)] for _ in range(M+1)] for _ in range(L)]

        for l in range(L):
            for m in range(M+1):
                for n in range(N+1):
                    cnt0, cnt1 = strs[l].count('0'), strs[l].count('1')
                    if l > 0 and m - cnt0 >= 0 and n-cnt1 >= 0:
                        dp[l][m][n] = max(dp[l][m][n], dp[l-1][m][n], dp[l-1][m-cnt0][n-cnt1]+1)
                    elif m - cnt0 >= 0 and n - cnt1 >= 0 :
                        dp[l][m][n] = max(dp[l][m][n], 1)
                    else :
                        dp[l][m][n] = max(dp[l][m][n], dp[l-1][m][n])

        #for l in range(L):
        #    for m in range(M+1):
        #        for n in range(N+1):
        #            print(f'LEVEL={l}, M={m}, N={n} : ', dp[l][m][n])

        return dp[-1][-1][-1]

