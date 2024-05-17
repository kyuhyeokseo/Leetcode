class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        gene_list = [startGene] + bank
        if endGene in bank :
            gene_list.remove(endGene)
            gene_list.append(endGene)
        if endGene not in gene_list :
            return -1
            
        N = len(gene_list)
        A = [[] for _ in range(N)]
        
        for i in range(N-1):
            for j in range(i+1, N) :
                x, y = gene_list[i], gene_list[j]
                if self.check_adj(x,y) == 1 :
                    A[i].append(j)
                    A[j].append(i)
                    
        visited = set()
        distance = [-1] * N
        q = deque()
        q.append(0)
        distance[0] = 0
                
        while q:
            node = q.popleft()

            for adj in A[node] :
                if adj in visited :
                    continue
                q.append(adj)
                visited.add(adj)
                distance[adj] = distance[node] + 1
                
        return distance[-1]
                
                
    def check_adj(self, x, y) :
        
        diff = 0
        for idx in range(len(x)):
            if x[idx] != y[idx] :
                diff += 1
        return diff
        
        
        
        
        
        