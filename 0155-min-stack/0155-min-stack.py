class MinStack:

    def __init__(self):
        self.stk = []
        self.minVal = -1
        self.min_stk = []

    def push(self, val: int) -> None:
        
        if len(self.stk) == 0 :
            self.minVal = val
            
        elif val <= self.minVal :
            self.minVal = val 

        self.min_stk.append(self.minVal)
        self.stk.append(val)

        #print('-------------------')
        #print(self.stk)
        #print(self.min_stk)
        

    def pop(self) -> None:
        tmp = self.stk.pop()
        tmp2 = self.min_stk.pop()
        if len(self.min_stk) > 0 :
            self.minVal = self.min_stk[-1]
        else :
            self.minVal = -1

        #print('-------------------')
        #print(self.stk)
        #print(self.min_stk)
        

    def top(self) -> int:
        #print('-------------------')
        #print(self.stk)
        #print(self.min_stk)
        
        return self.stk[-1]

    def getMin(self) -> int:
        #print('-------------------')
        #print(self.stk)
        #print(self.min_stk)
        
        return self.min_stk[-1]
    
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()