class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        nums.sort()
        mid = (L-1)//2
        print(nums)
        nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]

        