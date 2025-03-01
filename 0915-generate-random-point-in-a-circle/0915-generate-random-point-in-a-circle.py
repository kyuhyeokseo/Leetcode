import math, random

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.R = radius
        self.X = x_center
        self.Y = y_center


    def randPoint(self) -> List[float]:
        rand1, rand2 = sqrt(random.random()), random.random()
        D, theta = self.R * rand1, 2 * math.pi * rand2
        dX, dY = D * math.cos(theta), D * math.sin(theta)

        return [self.X + dX, self.Y + dY]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()