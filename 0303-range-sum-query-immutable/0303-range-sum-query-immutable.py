class NumArray:

    def __init__(self, nums: List[int]):
        
        S = 0
        self.accumulate = []
        for n in nums :
            self.accumulate.append(S)
            S += n
        self.accumulate.append(S)

    def sumRange(self, left: int, right: int) -> int:
        
        return self.accumulate[right+1] - self.accumulate[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)