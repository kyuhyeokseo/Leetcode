class MyCircularDeque:

    def __init__(self, k: int):
        self.DEQUE = []
        self.LIMIT = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.DEQUE = [value] + self.DEQUE
            return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.DEQUE.append(value)
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.DEQUE.pop(0)
            return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.DEQUE.pop()
            return True
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.DEQUE[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.DEQUE[-1]
        
    def isEmpty(self) -> bool:
        return len(self.DEQUE) == 0
        
    def isFull(self) -> bool:
        return len(self.DEQUE) == self.LIMIT


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()