# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node) -> List[int, bool]:
            if not node:
                return [0, True]

            left, right = 0, 0
            leftans, rightans = True, True
            if node.left:
                left, leftans = dfs(node.left)
            
            if node.right:
                right, rightans = dfs(node.right)
            
            if abs(left-right) <= 1 and leftans!=False and rightans!=False:
                boolans = True
            else:
                boolans = False
            
            return [1+max(left,right), boolans]
        
        _, boolans = dfs(root)

        return boolans
            
