# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dia(node):
            if not node:
                return 0
            
            h1 = dia(node.left)
            h2 = dia(node.right)
            diameter = h1+h2

            self.res = max(self.res, diameter)
            
            return max(h1, h2)+1
        
        dia(root)
        return self.res