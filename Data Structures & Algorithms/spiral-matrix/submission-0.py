class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        
        while l <= r and t <= b:
            for i in range(l, r + 1):
                ans.append(matrix[t][i])
            t += 1
            for j in range(t, b + 1):
                ans.append(matrix[j][r])
            r -= 1
            if not (l <= r and t <= b): break
            for k in range(r, l - 1, -1):
                ans.append(matrix[b][k])
            b -= 1
            for a in range(b, t - 1, -1):
                ans.append(matrix[a][l])
            l += 1
        return ans