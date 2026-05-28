class UnionFind:
    
    def __init__(self, n: int):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n
        
        for i in range(n):
            self.par[i] = i
            self.size[i] = 0

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        if self.find(x) == self.find(y):
            return True
        return False


    def union(self, x: int, y: int) -> bool:
        parentx = self.find(x)
        parenty = self.find(y)
        if parentx != parenty:
            if self.size[parentx] < self.size[parenty]:
                self.par[parentx] = parenty
                self.size[parenty] += self.size[parentx]
            else:
                self.par[parenty] = parentx
                self.size[parentx] += self.size[parenty]
            self.num_components -= 1
            return True
        return False
        

    def getNumComponents(self) -> int:
        return self.num_components

