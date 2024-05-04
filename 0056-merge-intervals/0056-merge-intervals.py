class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        ans = []
        
        for i in range(len(intervals)):
            x, y = intervals[i]
            #print('------------')
            #print(x,y)
            #print(ans)

            m, M = x, y
            
            remove_target = []
            for j in range(len(ans)):
                X, Y = ans[j]
                if (x-X) * (y-X) <= 0 or (x-Y) * (y-Y) <= 0 or (X<=x and Y>=y):
                    m = min(m, x, X)
                    M = max(M, y, Y)
                    remove_target.append([X, Y])
            for tmp in remove_target :
                ans.remove(tmp)
            ans.append([m, M])
            #print(ans)
        
        return ans

        
        
        
        