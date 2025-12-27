class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        N = len(nums)
        if N == 1:
            return 0 if target == nums[0] else -1
        elif N == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1
        else:
            mid = N // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                ret = self.search(nums[mid+1:], target)
                if ret < 0:
                    return -1
                else:
                    return mid + 1 + ret
            else:
                ret = self.search(nums[:mid], target)
                return ret