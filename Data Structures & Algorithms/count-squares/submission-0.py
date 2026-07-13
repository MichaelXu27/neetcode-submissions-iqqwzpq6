class CountSquares:

    def __init__(self):
        self.hashMap = {}


    def add(self, point: List[int]) -> None:
        self.hashMap[(point[0], point[1])] = self.hashMap.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total = 0
        for x2, y2 in self.hashMap.keys():
            if (abs(x2 - x1) != abs(y1 - y2) or x1 == x2 or y1 == y2):
                continue
            total += self.hashMap.get((x1, y2), 0) * self.hashMap.get((x2, y1), 0) * self.hashMap[(x2, y2)]
        return total
        
