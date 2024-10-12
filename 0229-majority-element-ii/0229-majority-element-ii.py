class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        L = len(nums)
        threshold = int(L//3)
        out = []
        
        num1 = num2 = -10**9 -1
        cnt1 = cnt2 = 0
        
        for n in nums :
            
            
            if num1 == n :
                cnt1 += 1
                
            elif num2 == n :
                cnt2 += 1
                
            elif cnt1 == 0 :
                num1 = n
                cnt1 += 1
            
            elif cnt2 == 0 :
                num2 = n
                cnt2 += 1
            
            else :
                cnt1 -= 1
                cnt2 -= 1
        
        print(num1, num2)
        
        cnt1 = cnt2 = 0
        for n in nums :
            if n == num1 :
                cnt1 += 1
            elif n == num2 :
                cnt2 += 1
        
        if cnt1 > threshold :
            out.append(num1)
        
        if cnt2 > threshold :
            out.append(num2)
        
        return out
        