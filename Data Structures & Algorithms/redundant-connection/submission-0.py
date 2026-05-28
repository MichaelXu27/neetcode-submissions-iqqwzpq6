class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.size = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.size[i] = 1
    
    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            if self.size[pa] > self.size[pb]:
                self.parent[pb] = pa
                self.size[pa] += self.size[pb]
            else:
                self.parent[pa] = pb
                self.size[pb] += self.size[pa]
            return True
        return False



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        unionObject = UnionFind(n)

        for start, end in edges:
            if not unionObject.union(start, end):
                return [start, end]
        return []

        