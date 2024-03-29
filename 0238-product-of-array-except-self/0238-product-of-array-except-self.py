class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        x, y = 1, 1

        answer = [1 for _ in range(L)]
        for i in range(L):
            
            a, b = nums[i], nums[L-1-i]

            x*= a
            y*= b

            if i+1 <= L-1:
                answer[i+1] *= x
                #print('x', i+1, x)
            if L-i-2>=0 :
                answer[L-i-2] *= y
                #print('y', L-i-2, y)

        #print(answer)
        return answer