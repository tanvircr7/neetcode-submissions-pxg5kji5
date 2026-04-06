# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        

        def f(node):
            if not node:
                return (0, True)
            
            h1, v1 = f(node.left)
            h2, v2 = f(node.right)

            thisbalanced = abs(h2-h1) <= 1
            thisheight = max(h1, h2) + 1

            if v1 == False or v2 == False or thisbalanced == False:
                return (thisheight, False)
            else:
                return (thisheight, True)
        
        height, val = f(root)

        return val
            
