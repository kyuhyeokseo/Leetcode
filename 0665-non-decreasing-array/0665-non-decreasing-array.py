class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        cnt = 0

        logN = None
        n = nums.pop()

        while nums:
            #print(nums, n, logN, cnt)
            if nums[-1] > n:
                cnt += 1
                if len(nums) == 1:
                    return cnt <= 1
                else:
                    if nums[-2] <= n:
                        nums[-1] = n
                    else:
                        n = nums.pop()
                        if logN and n > logN:
                            return False

            else:
                logN = n
                n = nums.pop()

            if cnt == 2:
                return False
        
        return True