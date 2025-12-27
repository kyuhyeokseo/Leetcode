class MyHashSet:

    def __init__(self):
        self.D = {}
        

    def add(self, key: int) -> None:
        self.D[key] = True

    def remove(self, key: int) -> None:
        if key in self.D:
            del self.D[key]
        
    def contains(self, key: int) -> bool:
        return key in self.D


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)