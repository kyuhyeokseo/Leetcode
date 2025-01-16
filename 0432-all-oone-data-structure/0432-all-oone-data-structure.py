class AllOne:

    def __init__(self):
        self.D = {}
        self.D_cnt = {}
        self.MAX = -1
        self.MIN = 100000

    def inc(self, key: str) -> None:
        if key in self.D :
            self.D[key] += 1
            cnt = self.D[key]
            if cnt in self.D_cnt :
                D_tmp = self.D_cnt[cnt]
                D_tmp[key] = True
            else :
                self.D_cnt[cnt] = {}
                self.D_cnt[cnt][key] = True
            del self.D_cnt[cnt-1][key]
            if not self.D_cnt[cnt-1]:
                del self.D_cnt[cnt-1]

        else :
            self.D[key] = 1
            if 1 in self.D_cnt:
                D_tmp = self.D_cnt[1]
                D_tmp[key] = True
            else :
                self.D_cnt[1] = {}
                self.D_cnt[1][key] = True

        self.MAX = max(self.MAX, self.D[key])
        self.MIN = min(self.MIN, self.D[key])
        if not self.MIN in self.D_cnt:
            self.MIN += 1
        
        #print('inc | ', key, ' | ', self.MAX, ' | ', self.MIN)
        #print(self.D_cnt)

    def dec(self, key: str) -> None:
        if key in self.D :
            self.D[key] -= 1
            cnt = self.D[key]
            if self.D[key] == 0 :
                del self.D[key]
            
            if cnt == 0 :
                D_tmp = self.D_cnt[cnt+1]
                del D_tmp[key]
                if not self.D_cnt[cnt+1]:
                    del self.D_cnt[cnt+1]

            else :
                D_tmp = self.D_cnt[cnt+1]
                del D_tmp[key]
                if not self.D_cnt[cnt+1]:
                    del self.D_cnt[cnt+1]

                if cnt in self.D_cnt :
                    D_tmp = self.D_cnt[cnt]
                    D_tmp[key] = True
                else :
                    self.D_cnt[cnt] = {}
                    self.D_cnt[cnt][key] = True
        
        if cnt > 0:
            self.MIN = min(self.MIN, cnt)
        else :
            if self.D_cnt:
                while self.MIN not in self.D_cnt:
                    self.MIN += 1
            else:
                self.MIN = 100000

        if not self.MAX in self.D_cnt:
            self.MAX -= 1
        
        #print('dec | ', key, ' | ', self.MAX, ' | ', self.MIN)
        #print(self.D_cnt)
        
    def getMaxKey(self) -> str:
        try:
            d_tmp = self.D_cnt[self.MAX]
            for item in d_tmp.keys():
                return item
        except:
            return ""

    def getMinKey(self) -> str:
        try:
            d_tmp = self.D_cnt[self.MIN]
            for item in d_tmp.keys():
                return item
        except:
            return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()