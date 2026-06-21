class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = {src: [] for src, dst in tickets}
        for src, dst in tickets:
            adjList[src].append(dst)
        target = len(tickets) + 1
        
        res = ["JFK"]
        
        def dfs(node):
            if len(res) == target:
                return True
            if node not in adjList:
                return False

            temp = adjList[node]
            for i, neigh in enumerate(temp):
                adjList[node].pop(i)
                res.append(neigh)
                if dfs(neigh): return True
                adjList[node].insert(i, neigh)
                res.pop()
        
        dfs("JFK")
        return res
                
        
        