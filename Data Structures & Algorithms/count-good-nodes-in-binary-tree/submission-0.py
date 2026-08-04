# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if node == None:
                return 0

            if node.val >= maxSoFar:
                maxSoFar = node.val
                return 1 + dfs(node.left, maxSoFar) + dfs(node.right, maxSoFar)
            else:
                return dfs(node.left, maxSoFar) + dfs(node.right, maxSoFar)
        
        return dfs(root, root.val)
        
        