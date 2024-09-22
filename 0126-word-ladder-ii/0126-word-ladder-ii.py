class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordSet = set(wordList) 
        wordSet.discard(beginWord)
        
        P = defaultdict(set)
        
        def findParent(word):
            
            path_list = [[word]]
            
            while True:
                new = []
                for path in path_list:
                    curr = path[0]
                    if curr == beginWord:
                        return path_list
                        
                    parent_list = P[curr]

                    for parent in parent_list :

                        new.append([parent] + path[:])

                path_list = new[:]
            
            return [[]]
                    
            
        
        def neighbor(word):
            adj = []
            for j in range(len(word)): 
                for c in ascii_lowercase:
                    newWord = word[:j] + c + word[j + 1:]
                    if newWord in wordSet:
                        adj.append(newWord)
            return adj[:]
            
        
        level = []
        level.append(beginWord)
        
        while level:
            #print(level)
            nxt = set()
            for word in level:
                if word == endWord:
                    #print(P)
                    return findParent(endWord)
                for nei in neighbor(word):
                    P[nei].add(word)
                    nxt.add(nei)
                    
            wordSet -= set(nxt)
            level = list(nxt)[:]
            
        return []

        
                
                
                
                