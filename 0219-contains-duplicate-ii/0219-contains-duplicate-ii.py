class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)) :
            if i>k :
                del d[nums[i-k-1]]
            target = nums[i]
            if target in d :
                return True
            else :
                d[target] = 1
        return False