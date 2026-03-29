# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def di(node):
            if not node:
                return 0
            
            l = di(node.left)
            r = di(node.right)

            diameter = l+r

            self.res = max(self.res, diameter)

            return 1+max(l,r)

        
        di(root)
        return self.res