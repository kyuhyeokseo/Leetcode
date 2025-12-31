class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)

        def CountPairs(distance):
            left = 0
            ret = 0
            for right in range(1, len(nums)):
                while left < right and nums[right] - nums[left] > distance:
                    left += 1
                ret += (right - left)
            return ret


        minDistance, maxDistance = 0, nums[-1] - nums[0]

        while minDistance < maxDistance:
            midDistance = (minDistance + maxDistance) // 2
            cnt = CountPairs(midDistance)
            if cnt < k:
                minDistance = midDistance + 1
            else:
                maxDistance = midDistance
        
        return minDistance
