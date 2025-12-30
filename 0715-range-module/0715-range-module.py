class RangeModule:

    def __init__(self):
        MAX = 10 ** 9 + 1
        self.intervals = [[-2, -1], [MAX, MAX+1]]

    def overlap(self, n):
        for i in range(len(self.intervals)-1):
            l1, r1 = self.intervals[i]
            l2, r2 = self.intervals[i+1]
            if l1 <= n <= r1:
                return i, True
            elif r1 < n < l2:
                return i+1, False

    def addRange(self, left: int, right: int) -> None:
        idx1, o1 = self.overlap(left)
        idx2, o2 = self.overlap(right)

        if idx1 == idx2:
            if not o1 and not o2:
                self.intervals = self.intervals[:idx1] + [[left, right]] + self.intervals[idx2:]
            elif o1 != o2:
                self.intervals[idx1] = [min(left, self.intervals[idx1][0]), max(right, self.intervals[idx1][1])]
        else:
            if not o1 and not o2:
                self.intervals = self.intervals[:idx1] + [[left, right]] + self.intervals[idx2:]
            elif not o1 and o2:
                self.intervals[idx2] = [min(left, self.intervals[idx2][0]), max(right, self.intervals[idx2][1])]
                self.intervals = self.intervals[:idx1] + self.intervals[idx2:]
            elif o1 and not o2:
                self.intervals = self.intervals[:idx1] + [[min(left, self.intervals[idx1][0]), right]] + self.intervals[idx2:]
            else:
                self.intervals[idx2] = [min(left, self.intervals[idx1][0]), max(right, self.intervals[idx2][1])]
                self.intervals = self.intervals[:idx1] + self.intervals[idx2:]

        #print(self.intervals)


    def queryRange(self, left: int, right: int) -> bool:
        idx1, o1 = self.overlap(left)
        idx2, o2 = self.overlap(right)
        return idx1==idx2 and o1 and o2
        
    def removeRange(self, left: int, right: int) -> None:
        idx1, o1 = self.overlap(left)
        idx2, o2 = self.overlap(right)

        if idx1 == idx2:
            x1, x2 = self.intervals[idx1]
            if o1 and o2:
                tmp = []
                if left > x1:
                    tmp.append([x1, left])
                if x2 > right:
                    tmp.append([right, x2])
                self.intervals = self.intervals[:idx1] + tmp[:] + self.intervals[idx2+1:]
            elif o1 != o2:
                if right < x2:
                    self.intervals[idx1][0] = right
                else:
                    self.intervals =  self.intervals[:idx1] +  self.intervals[idx1+1:]
        else:
            if not o1 and not o2:
                self.intervals = self.intervals[:idx1] + self.intervals[idx2:]
            elif not o1 and o2:
                x1, x2 = self.intervals[idx2]
                if right < x2:
                    self.intervals[idx2][0] = right
                    self.intervals = self.intervals[:idx1] + self.intervals[idx2:]
                else:
                    self.intervals = self.intervals[:idx1] + self.intervals[idx2+1:]
            elif o1 and not o2:
                x1, x2 = self.intervals[idx1]
                if x1 < left:
                    self.intervals = self.intervals[:idx1] + [[x1, left]] + self.intervals[idx2:]
                else:
                    self.intervals = self.intervals[:idx1] + self.intervals[idx2:]
            else:
                self.removeRange(left, (self.intervals[idx1][1]+self.intervals[idx1+1][0])/2)
                self.removeRange((self.intervals[idx1][1]+self.intervals[idx1+1][0])/2, right)
        
        #print(self.intervals)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)