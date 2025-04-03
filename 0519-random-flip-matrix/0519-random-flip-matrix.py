class Solution:

    def __init__(self, m: int, n: int):
        self.C = m * n
        self.M = m
        self.N = n
        self.limit = m * n
        self.used = set()
        

    def flip(self) -> List[int]:

        rand = random.randint(0, self.C-1)
        while rand in self.used:
            rand += 1
            if rand == self.limit:
                rand = 0
        self.used.add(rand)

        return [rand//self.N, rand%self.N]
        

    def reset(self) -> None:
        self.used = set()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()