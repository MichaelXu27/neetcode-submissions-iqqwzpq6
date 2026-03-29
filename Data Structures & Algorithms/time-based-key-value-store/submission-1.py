class TimeMap:

    def __init__(self):
        self.dic = {} # key:[(timestamp, value)]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [(timestamp, value)]
        else:
            self.dic[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        arr = self.dic[key]
        left, right = 0, len(arr) - 1
        prev = left
        if timestamp >= arr[right][0]:
            return arr[-1][1]
        elif timestamp < arr[left][0]:
            return ""
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] > timestamp:
                right = mid - 1
            elif arr[mid][0] < timestamp:
                prev = mid
                left = mid + 1
            else:
                return arr[mid][1]
        return arr[prev][1]  


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)