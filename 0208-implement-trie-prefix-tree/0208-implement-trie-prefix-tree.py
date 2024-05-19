class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()
        self.done = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)) :
            tmp = word[i]
            if tmp not in curr.children :
                prefix = word[0:i+1]
                curr.children[tmp] = TrieNode(prefix)
            curr = curr.children[tmp]
        curr.done = True
            

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)) :
            tmp = word[i]
            if tmp not in curr.children :
                return False
            curr = curr.children[tmp]
        if curr is not None :
            if curr.done == True :
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)) :
            tmp = prefix[i]
            if tmp not in curr.children :
                return False
            curr = curr.children[tmp]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

