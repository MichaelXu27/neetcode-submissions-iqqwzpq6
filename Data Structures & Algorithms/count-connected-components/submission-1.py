class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adjList = {i: [] for i in range(n)}
        total = 0

        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)

        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            
            for neigh in adjList[node]:
                if neigh == parent:
                    continue
                dfs(neigh, node)
        
        for i in range(n):
            if i in visited:
                continue
            dfs(i, -1)
            total += 1
        return total