class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0]* capacity
        self.index = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) == self.index:
            self.resize()
        self.array[self.index] = n
        self.index += 1
            

    def popback(self) -> int:
        self.index -= 1
        return self.array[self.index]

    def resize(self) -> None:
        newList = [0] * self.capacity * 2
        for i, elem in enumerate(self.array):
            newList[i] = elem
        self.array = newList
        self.capacity *= 2
        

    def getSize(self) -> int:   
        return self.index
    
    def getCapacity(self) -> int:
        return self.capacity