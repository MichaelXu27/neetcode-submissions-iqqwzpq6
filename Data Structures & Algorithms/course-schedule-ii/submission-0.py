class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            adjList[b].append(a)


        ans = []
        visited = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            

            visiting.add(node)
            for neigh in adjList[node]:
                if not dfs(neigh):
                    return False

            visiting.remove(node)
            visited.add(node)
            ans.append(node)

            return True



        for node in adjList.keys():
            if not dfs(node):
                return []

        return ans[::-1]

            