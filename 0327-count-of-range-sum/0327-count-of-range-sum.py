class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        
        S = [0 for _ in range(len(nums))]
        self.ret = 0
        
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s >= lower and s <= upper :
                self.ret += 1
            S[i] = s
        
        
        def conquer(left, right):
            
            #print('----------------------')
            #print(left, right)
            r1, r2 = 0, 0
            
            for i in range(len(left)):

                sumL = left[i]
                while r1 < len(right) and right[r1]-sumL < lower :
                    r1 += 1
                while r2 < len(right) and right[r2]-sumL <= upper :
                    r2 += 1

               
                self.ret += r2 - r1
            
            out = []
            i, j = 0, 0
            
            while i < len(left) and j < len(right) :
                if left[i] <= right[j] :
                    out.append(left[i])
                    i += 1
                else :
                    out.append(right[j])
                    j += 1
            
            return out + left[i:] + right[j:]
        
        
        def divide(num_array):
            
            L = len(num_array)
            
            if L == 1 :
                return num_array
            else :
                mid = L // 2
                left_array = divide(num_array[:mid])
                right_array = divide(num_array[mid:])
                return conquer(left_array, right_array)
        
        divide(S)
        return self.ret
        
        
        