class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        L = len(triangle)
        dp = [triangle[0][0]]
        
        out = 1001 * 200
        
        if L == 1 :
            return triangle[0][0]
        
        for lv in range(1, L) :
            
            tmp = []
            
            if lv == L-1 :
                
                for idx in range(len(triangle[lv])) :

                    if idx == 0 :
                        tmp.append(dp[idx] + triangle[lv][idx])
                        out = min(out, dp[idx] + triangle[lv][idx])
                    elif idx == len(triangle[lv]) -1 :
                        tmp.append(dp[idx-1] + triangle[lv][idx])
                        out = min(out, dp[idx-1] + triangle[lv][idx])
                    else :
                        tmp.append(min(dp[idx], dp[idx-1]) + triangle[lv][idx])
                        out = min(out, min(dp[idx], dp[idx-1]) + triangle[lv][idx])

                dp = tmp.copy()
                    
            else :
                for idx in range(len(triangle[lv])) :

                    if idx == 0 :
                        tmp.append(dp[idx] + triangle[lv][idx])
                    elif idx == len(triangle[lv]) -1 :
                        tmp.append(dp[idx-1] + triangle[lv][idx])
                    else :
                        tmp.append(min(dp[idx], dp[idx-1]) + triangle[lv][idx])

                dp = tmp.copy()
                    
        return out
        