import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        
        self.tot = 0
        self.S, self.X, self.Y = [], [], []

        self.rects = []
        # For each rectangle, there are (x_i - a_i + 1) * (y_i - b_i + 1) integer points
        for rect in rects:
            a,b,x,y = rect[0], rect[1], rect[2], rect[3]
            self.tot += (x-a+1) * (y-b+1)
            self.S.append(self.tot)
            self.X.append([x,a])
            self.Y.append([y,b])
            

    def pick(self) -> List[int]:
        rand = random.randint(0, self.tot-1)

        i = 0
        while rand >= self.S[i]:
            i += 1
        
        if i > 0:
            rand -= self.S[i-1]

        a,b,x,y = self.X[i][1], self.Y[i][1], self.X[i][0], self.Y[i][0]
        du, dv = rand % (x-a+1), rand // (x-a+1)

        return [a+du, b+dv]