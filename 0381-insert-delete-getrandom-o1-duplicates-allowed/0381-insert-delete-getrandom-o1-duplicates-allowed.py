

class RandomizedCollection:

    def __init__(self):
        self.store = []
        self.map = {}
        self.N = 0

    def insert(self, val: int) -> bool:
        
        self.store.append(val)
        if val in self.map :
            self.map[val].append(self.N)
            self.N += 1
            
            return False
        
        else :
            self.map[val] = [self.N]
            self.N += 1
            
            return True
        
        
        

    def remove(self, val: int) -> bool:

        
        if val in self.map :
            self.N -= 1
            
            last = self.map[val].pop()
            
            V = self.store[-1]
            
            if val != V :
                self.store[last] = V
                self.store.pop()
                self.map[V].remove(self.N)
                self.map[V].append(last)
                self.map[V].sort()
                
            else :
                self.store.pop()
            
            if not self.map[val] :
                del self.map[val]
        
        
            #print(f'Delete {val}')
            #print(self.store)
            #print(self.map)
        
            return True
        
        else :
            #print(f'Delete {val}')
            #print(self.store)
            #print(self.map)
            return False
        
        
    def getRandom(self) -> int:
        return random.choice(self.store)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()