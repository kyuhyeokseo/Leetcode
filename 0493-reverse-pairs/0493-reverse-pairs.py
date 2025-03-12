class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.cnt = 0

        merged = self.mergeSort(nums)
        return self.cnt

    def mergeSort(self, nums):
        if len(nums) < 2 :
            return nums
        
        mid = len(nums) // 2
        left  = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])

        merged = []
        x = y = 0
        L = len(left)
        while x < len(left) and y < len(right):
            if left[x] > 2*right[y] :
                self.cnt += (L-x)
                y += 1
            else :
                x += 1

        x = y = 0
        while x < len(left) and y < len(right):
            if left[x] <= right[y]:
                merged.append(left[x])
                x += 1
            else :
                merged.append(right[y])
                y += 1
        merged += left[x:]
        merged += right[y:]

        return merged