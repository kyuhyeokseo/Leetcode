class MyCalendar:

    def __init__(self):

        self.reserved = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        
        if not self.reserved:
            self.reserved = [[startTime, endTime]]
            return True

        for i, res in enumerate(self.reserved):
            if endTime > res[0] and startTime < res[1]:
                return False
            elif endTime <= res[0]:
                self.reserved = self.reserved[:i] + [[startTime, endTime]] + self.reserved[i:]
                return True

        self.reserved.append([startTime, endTime])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)