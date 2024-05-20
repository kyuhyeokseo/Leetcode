class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end=True
        

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
        
        
        
    def dfs(self, curr, word, idx) :
        
        if idx == len(word) :
            return curr.end
        
        if word[idx] == '.' :
            for children_node in curr.children.values():
                if self.dfs(children_node, word, idx+1) :
                    return True
            return False
        
        if word[idx] not in curr.children :
            return False
        
    
        return self.dfs(curr.children[word[idx]], word, idx+1)
        
        
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)