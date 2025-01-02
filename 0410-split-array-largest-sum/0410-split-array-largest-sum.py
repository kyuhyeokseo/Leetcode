class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        Low, High = max(nums), sum(nums)

        while Low < High :
            Mid = (Low + High) // 2
            eachSum, subCnt = 0, 1

            for n in nums :
                if eachSum + n <= Mid :
                    eachSum += n
                else :
                    eachSum = n
                    subCnt += 1
            
            if subCnt > k :
                Low = Mid + 1
            else :
                High = Mid
        
        return High

