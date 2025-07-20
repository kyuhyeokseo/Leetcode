class MapSum:

    def __init__(self):
        self.D = {}
        self.key_list = []
        
    def insert(self, key: str, val: int) -> None:
        if key not in self.D:
            self.key_list.append(key)
        self.D[key] = val
        

    def sum(self, prefix: str) -> int:
        L = len(prefix)
        ret = 0
        for key in self.key_list:
            if len(key) < L:
                pass
            else:
                if key[:L] == prefix:
                    ret += self.D[key]
        
        return ret
            


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)