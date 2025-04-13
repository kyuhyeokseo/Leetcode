class Solution:

    def __init__(self, w: List[int]):
        self.range = [0]
        s = 0
        for wei in w:
            s += wei
            self.range.append(s)
        self.S = s

    def pickIndex(self) -> int:

        rand = random.randint(1, self.S)

        i, j = 0, len(self.range)
        mid = (i+j) // 2

        while i <= j:
            mid = (i+j+1) // 2

            if self.range[mid-1] < rand and rand <= self.range[mid]:
                return mid-1
            
            elif self.range[mid-1] >= rand:
                j = mid-1
            elif self.range[mid] < rand:
                i = mid
        
        return -1







# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()