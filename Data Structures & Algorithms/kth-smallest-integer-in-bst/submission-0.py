# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, valuesList):
            if node is None:
                return
            
            valuesList.append(node.val)
            dfs(node.left, valuesList)
            dfs(node.right, valuesList)
        
        valuesList = []
        dfs(root, valuesList)
        valuesList.sort()

        minValue = 0
        while k:
            minValue = valuesList.pop(0)
            k -= 1
        
        return minValue


        
            

            

            

        