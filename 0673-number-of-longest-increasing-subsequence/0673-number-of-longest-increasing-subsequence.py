class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        L = len(nums)
        consecs = [[1, 1] for _ in range(L)]
        # [MAX Length of subseq ending with n, # of subseq]

        if L == 1:
            return 1

        maxL, ret = 0, 0

        for i in range(0, L):
            for j in range(0, i):

                if nums[j] < nums[i]:
                    if consecs[j][0] + 1 == consecs[i][0]:
                        consecs[i][1] += consecs[j][1]
                    elif consecs[j][0] + 1 > consecs[i][0]:
                        consecs[i][0] = consecs[j][0] + 1
                        consecs[i][1] = consecs[j][1]
                
            if consecs[i][0] == maxL:
                ret += consecs[i][1]
            elif consecs[i][0] > maxL:
                maxL = consecs[i][0]
                ret = consecs[i][1]

        return ret
        
