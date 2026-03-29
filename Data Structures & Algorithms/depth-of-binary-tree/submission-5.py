# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        

        def f(node):
            if not node:
                return 0
            
            h1 = f(node.left)
            h2 = f(node.right)

            return max(h1, h2) + 1
        
        return f(root)