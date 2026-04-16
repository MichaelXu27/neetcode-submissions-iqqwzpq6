# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        def bfs(node):
            q = deque()
            q.append(node)
            while q:
                n = len(q)
                temp = []
                for _ in range(n):
                    popped = q.popleft()
                    if not popped:
                        continue
                    temp.append(popped.val)
                    q.append(popped.left)
                    q.append(popped.right)
                if temp:
                    self.ans.append(temp) 
        bfs(root)
        return self.ans                  