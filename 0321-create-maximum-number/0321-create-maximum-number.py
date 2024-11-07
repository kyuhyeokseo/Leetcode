class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        M, N = len(nums1), len(nums2)
        K = k
        R = M + N - K
        
        ret = [0] * K
        
        for x in range(K+1):
            y = K-x
            
            if x <= M and y <= N :
                
                X = self.getMax(nums1, x)
                Y = self.getMax(nums2, y)
                new = self.mergeXY(X, Y)
                print(x,y,X, Y, new)
                ret = max(ret, new)
                
        return ret
        
        
        
    def getMax(self, nums, L):
        
        out = []
        
        for i in range(len(nums)) :
            
            n = nums[i]
            if len(out) == 0 :
                out.append(n)
            elif out[-1] >= n :
                out.append(n)
            else :
                while out and out[-1] < n and (len(nums) - i + len(out) -1) >= L :
                    out.pop()
                out.append(n)
        
        return out[:L]
        
        
    def mergeXY(self, X, Y):
        
        out = []
        
        while X or Y :
            if X > Y :
                out.append(X[0])
                X = X[1:]
            else :
                out.append(Y[0])
                Y = Y[1:]
        
        return out
        
        
        