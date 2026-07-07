class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = {}
        n = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in lastSeen:
                lastSeen[s[i]] = i
        
        pivot = 0
        ans = []
        for i, char in enumerate(s):
            farthest = lastSeen[char]
            
            if i > pivot:
                ans.append(i)
            pivot = max(pivot, farthest)
        
        ans.append(n)
        newAns = [ans[0]]
        for i in range(len(ans) - 1):
            newAns.append(ans[i + 1] - ans[i])
        return newAns
        

            
            
