class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjList = {i: [] for i in range(n)}

        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            
            for neigh in adjList[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            
            return True

        res = dfs(0, -1)

        return res if len(visited) == n else False

    