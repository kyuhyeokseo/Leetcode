class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        q = deque()
        q.append(beginWord)
        
        if endWord not in wordList :
            return 0
        
        if beginWord not in wordList :
            wordList.append(beginWord)
        d_adj = {}
        distance = {}
        visited = {}
        L = len(wordList)
        
        for item in wordList :
            d_adj[item]=[]
            distance[item] = 0
            visited[item] = False
        
        for x in range(L-1) :
            srt = wordList[x]

            
            for y in range(x+1, L) :
                end = wordList[y]
                
                if self.get_diff(srt, end) == 1 :
                    d_adj[srt].append(end)
                    d_adj[end].append(srt)
                    
        visited[beginWord] = True
        #print(d_adj)
        
        while q : 

            curr = q.popleft()
            for nei in d_adj[curr] :
                if visited[nei] == False :
                    q.append(nei)
                    distance[nei] = distance[curr] + 1
                    visited[nei] = True
                    if nei == endWord :
                        return distance[endWord] + 1
        
        return distance[endWord] 
            
            
            
            
    def get_diff(self, x, y) :
        diff = 0
        for idx in range(len(x)) :
            if x[idx] != y[idx] :
                diff += 1
        return diff
        
        
        
        
        
        
        