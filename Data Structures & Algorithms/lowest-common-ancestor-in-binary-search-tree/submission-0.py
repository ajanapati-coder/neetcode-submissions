# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        currentLowest = root

        while currentLowest != None:
            if p.val < currentLowest.val and q.val < currentLowest.val:
                currentLowest = currentLowest.left
            elif p.val > currentLowest.val and q.val > currentLowest.val:
                currentLowest = currentLowest.right
            elif p.val < currentLowest.val and q.val > currentLowest.val:
                return currentLowest
            elif p.val > currentLowest.val and q.val < currentLowest.val:
                return currentLowest
            elif p.val == currentLowest.val:
                currentLowest = p
                return currentLowest
            elif q.val == currentLowest.val:
                currentLowest = q
                return currentLowest
        
        return currentLowest
        
        