class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.C = 0
        self.d = {}
        self.lru = []

    def get(self, key: int) -> int:
        if key in self.d :
            self.lru.remove(key)
            self.lru.append(key)
            #print(self.d)
            #print(self.lru)
            return self.d[key]
        else :
            #print(self.d)
            #print(self.lru)
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.d :
            self.lru.remove(key)
            self.lru.append(key)
            self.d[key] = value
        else :
            self.d[key] = value
            if self.C == self.capacity :
                target = self.lru[0]
                self.lru[:] = self.lru[1:]
                del self.d[target]
                self.lru.append(key)
            else :
                self.C += 1
                self.lru.append(key)
        
        #print(self.d)
        #print(self.lru)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)