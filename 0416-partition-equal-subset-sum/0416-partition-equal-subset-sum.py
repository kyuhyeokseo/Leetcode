class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        S = sum(nums)
        if S % 2 == 1 or len(nums) == 1 :
            return False 
        
        TARGET = S // 2

        C = [[nums[0], 0]]

        for i in range(1, len(nums)) :

            n = nums[i]

            C_tmp = set()
            for curr in C :
                if curr[0] + n < TARGET :
                    C_tmp.add(str(curr[0] + n) + '_' + str(curr[1]))
                elif curr[0] + n == TARGET :
                    return True

                if curr[1] + n < TARGET :
                    C_tmp.add(str(curr[0]) + '_' + str(curr[1] + n))
                elif curr[1] + n == TARGET :
                    return True
            
            C = []
            for item in list(C_tmp):
                x = item.split('_')
                C.append([int(x[0]), int(x[1])])

        return False

