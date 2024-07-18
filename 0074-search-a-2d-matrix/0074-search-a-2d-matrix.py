class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        first_column = [row[0] for row in matrix]
        
        
        targetR = self.searchRow(first_column, target)
        #print('--------------')
        targetC = self.searchRow(matrix[targetR], target)
        #print(targetR, targetC)
        
        
        if target == matrix[targetR][targetC] :
            return True
        else :
            return False
        
        
    def searchRow(self, nums : List[int], target : int) -> int :
        #print(nums)
        
        L = len(nums)
        if L == 1 : 
            return 0

            
        center_idx = int(L//2)
        center_num = nums[center_idx]
        
        if target == center_num :
            return center_idx
        elif target < center_num :
            return self.searchRow(nums[:center_idx], target)
        else :
            return center_idx + self.searchRow(nums[center_idx:], target)
        
        
            