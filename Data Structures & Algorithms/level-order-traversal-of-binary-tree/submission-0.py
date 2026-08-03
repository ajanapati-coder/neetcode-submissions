# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root == None:
            return result

        queue = [root]

        while queue:
            currentLevel = []
            currentLength = len(queue)

            while currentLength:
                tree = queue.pop(0)
                if tree != None:
                    currentLevel.append(tree.val)
                    queue.append(tree.left)
                    queue.append(tree.right)
                currentLength -= 1
            
            if currentLevel != []:
                result.append(currentLevel)
        
        return result

            

        