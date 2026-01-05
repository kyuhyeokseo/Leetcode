class MyCalendarThree:

    def __init__(self):

        self.delta = {}
        self.max_k = 0

    def book(self, startTime: int, endTime: int) -> int:

        if startTime in self.delta:
            self.delta[startTime] += 1
        else:
            self.delta[startTime] = 1

        if endTime in self.delta:
            self.delta[endTime] -= 1
        else:
            self.delta[endTime] = -1

        curr = 0
        for key in sorted(list(self.delta.keys())):
            curr += self.delta[key]
            if curr > self.max_k:
                self.max_k = curr

        return self.max_k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)