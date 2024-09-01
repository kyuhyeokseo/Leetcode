class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        N = len(heights)
        
        MAX_A = 0
        stack = []
        
        for i in range(N+1):
            
            new_H = 0 if i == N else heights[i]
            
            #print('-----------------')
            #print(i, new_H)
            
            while len(stack) > 0 and new_H < heights[stack[-1]] :
                
                
                I = stack.pop()
                W = i-stack[-1]-1 if stack else i
                H = heights[I]
                A = W * H
                #print(I, W, H, A)
                MAX_A = max(MAX_A, A)
            
            stack.append(i)
        
        
        return MAX_A
        
        
        
        
        