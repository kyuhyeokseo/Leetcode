class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        self.Path_to = defaultdict(list)
        self.ret = []
        
        N = len(tickets)
        tickets.sort()
        
        self.tickets = tickets
        
        for ticket in self.tickets :
            self.Path_to[ticket[0]].append(ticket[1])
            
        print(self.Path_to)
        
        self.visit('JFK')
        return self.ret[::-1]
        
            
    def visit(self, city) :
        while self.Path_to[city] :
            self.visit(self.Path_to[city].pop(0))
        self.ret.append(city)
        
                
        
            
        
        
        
        
        
        
        
        
        