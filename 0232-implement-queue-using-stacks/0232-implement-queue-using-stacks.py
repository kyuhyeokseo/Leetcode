class MyQueue:

    def __init__(self):
        self.X = []
        

    def push(self, x: int) -> None:
        self.X.append(x)

    def pop(self) -> int:
        a = self.X[0]
        self.X = self.X[1:]
        return a

    def peek(self) -> int:
        return self.X[0]

    def empty(self) -> bool:
        return (len(self.X) == 0)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()