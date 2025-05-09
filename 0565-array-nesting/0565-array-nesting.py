class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        f = nums[:]
        n = len(nums)
        ret = 0
        visited = [False for _ in range(n)]

        for k in range(n):
            
            if not visited[k]:
                visited[k] = True
                x, y = k, f[k]
                X = set()
                Y = set()
                X.add(x)
                Y.add(y)
                
                while X != Y:
                    x = y
                    y = f[x]
                    visited[x] = True
                    X.add(x)
                    Y.add(y)

                ret = max(ret, len(X))
        
        return ret
