# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftLim, rightLim):
            if not node:
                return True
            if not (leftLim < node.val < rightLim):
                return False
            
            return dfs(node.left, leftLim , node.val) and dfs(node.right, node.val, rightLim)
        return dfs(root, float('-inf'), float('inf'))
            