class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L = len(height)
        H = 0
        result = 0
        
        x = 0
        y = L-1
        
        while x < y :
            result = max(result, (y-x) * min(height[x], height[y]))
            if height[x] < height[y] :
                x += 1
            else :
                y -= 1
        
        return result 
            
            
            
        
        
        
        
        
        