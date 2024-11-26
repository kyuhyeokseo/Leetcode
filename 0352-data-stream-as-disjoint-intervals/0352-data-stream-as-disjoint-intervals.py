class SummaryRanges:

    def __init__(self):
        self.interval = []

    def addNum(self, value: int) -> None:
        
        if len(self.interval) == 0 :
            self.interval.append([value, value])
        else :
            srt_idx, end_idx = -1, -1
            new_idx = 0
            
            for i, itv in enumerate(self.interval) :
                if value - itv[1] == 1 :
                    end_idx = i
                if itv[0] - value == 1 :
                    srt_idx = i
                if value > itv[1] :
                    new_idx = i+1
                if itv[0] <= value and value<=itv[1] :
                    new_idx = -99
            
            if new_idx != -99 :
                if end_idx == srt_idx == -1:
                    self.interval = self.interval[:new_idx] + [[value, value]] + self.interval[new_idx:]
                elif srt_idx == -1 and end_idx != -1:
                    self.interval[end_idx][1] = value
                elif srt_idx != -1 and end_idx == -1:
                    self.interval[srt_idx][0] = value
                else:
                    self.interval[end_idx][1] = self.interval[srt_idx][1]
                    self.interval = self.interval[:srt_idx] + self.interval[srt_idx+1:]
            
        #print(self.interval)
        

    def getIntervals(self) -> List[List[int]]:
        return self.interval
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()