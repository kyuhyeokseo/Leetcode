class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        W = len(height)
        left = [0]
        right = [0]
        
        result = 0
        
        max_L = 0
        max_R = 0
        for w in range(W):
            if w > 0 :
                max_L = max(max_L, height[w-1])
                max_R = max(max_R, height[W-w])
                left.append(max_L)
                right.append(max_R)
                
        for w in range(W):
            result += max(0, min(left[w], right[W-1-w]) - height[w])
        
        
        return result
        
        
        
        
        
        
        
        