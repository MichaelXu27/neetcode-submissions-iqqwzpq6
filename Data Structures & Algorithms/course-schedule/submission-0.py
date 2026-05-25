class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}

        for course in prerequisites:
            adjList[course[1]].append(course[0])
        
        def dfs(node):
            nonlocal visiting
            if node in visiting:
                return False
            visiting.add(node)
            for neigh in adjList[node]:
                if not dfs(neigh):
                    return False
            visiting.remove(node)
            return True
            
        
        for node in adjList.keys():
            visited = set()
            visiting = set()
            if node in visited:
                continue
            visited.add(node)
            
            if not dfs(node):
                return False
            
        return True
