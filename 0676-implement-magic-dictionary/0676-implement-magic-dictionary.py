class MagicDictionary:

    def __init__(self):
        self.D = defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for s in dictionary:
            self.D[len(s)].append(s)

    def search(self, searchWord: str) -> bool:
        L = len(searchWord)

        if L not in self.D:
            return False
        elif not self.D[L]:
            return False
        else:
            candidates = self.D[L]
            for i in range(L):
                y = searchWord[:i] + searchWord[i+1:]

                for target in candidates:
                
                    x = target[:i] + target[i+1:]
                    if x == y and target[i] != searchWord[i]:
                        return True
            return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)