# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if root != None:
            queue = [root]
        else:
            return result

        while queue:
            currLevel = []
            currLength = len(queue)

            while currLength:
                tree = queue.pop(0)
                if tree != None:
                    currLevel.append(tree.val)
                    queue.append(tree.left)
                    queue.append(tree.right)
                currLength -= 1
            
            if currLevel != []:
                result.append(currLevel.pop())
        
        return result



        