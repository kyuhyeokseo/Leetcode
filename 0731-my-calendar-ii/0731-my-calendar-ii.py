class MyCalendarTwo:

    def __init__(self):

        self.reserved_1 = []
        self.reserved_2 = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        
        if not self.reserved_1:
            self.reserved_1 = [[startTime, endTime]]
            return True

        for i, res in enumerate(self.reserved_2):
            if endTime > res[0] and startTime < res[1]:
                return False

        for i, res in enumerate(self.reserved_1):
            if max(startTime, res[0]) < min(endTime, res[1]):
                self.reserved_2.append([max(startTime, res[0]), min(endTime, res[1])])


        self.reserved_1.append([startTime, endTime])

        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)