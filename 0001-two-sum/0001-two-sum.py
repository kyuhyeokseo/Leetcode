class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        temp = []
        for idx in range(len(nums)):
            d[nums[idx]] = idx
            if nums[idx] == target//2 and target % 2 == 0 :
                temp.append(idx)
        
        if len(temp) == 2 :
            return temp
        
        for item in nums :
            remain = target - item
            if remain != item :
                if remain in d :
                    return [d[item], d[remain]]