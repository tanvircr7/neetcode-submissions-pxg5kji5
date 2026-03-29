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
        
        def dfs(node,dis):
            if node is None:
                return dis
            
            dis1 = dfs(node.left, dis+1)
            dis2 = dfs(node.right, dis+1)

            return max(dis1, dis2)

        return dfs(root,0)
        
        