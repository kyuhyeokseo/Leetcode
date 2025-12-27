class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.N, self.M = n, n-len(blacklist)
        self.map = {target: 1 for target in blacklist}
        srt = n-1

        for target in self.map:
            if target < self.M:
                
                while srt in self.map:
                    srt -= 1
                self.map[target] = srt
                srt -= 1

    def pick(self) -> int:
        r = random.randint(0, self.M-1)
        if r in self.map:
            return self.map[r]
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()