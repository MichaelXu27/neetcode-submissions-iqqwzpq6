class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i, j, k = 0, 0, 0
        n1, n2, n3, = len(s1), len(s2), len(s3)

        memo = {}

        if n3 != n1 + n2:
            return False

        def search(i, j, k):
            if k == len(s3):
                return True
            else:
                if (i,j) in memo:
                    return memo[(i,j)]
                res = False
                if i < len(s1) and s1[i] == s3[k]:
                    res = search(i + 1, j, k + 1)
                if not res and j < len(s2) and s2[j] == s3[k]:
                    res = search(i, j + 1, k + 1)
                
                memo[(i,j)] = res
                return res

        return search(0, 0, 0)
            