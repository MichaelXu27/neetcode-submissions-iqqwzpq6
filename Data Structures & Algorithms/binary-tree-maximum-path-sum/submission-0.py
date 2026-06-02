# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            cur = node.val
            

            maxSum = max(maxSum, cur + right, cur + left + right)

            return max(cur, cur + left, cur + right)
        
        dfs(root)
        return maxSum
            
        