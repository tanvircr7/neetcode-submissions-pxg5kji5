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
        
        def dfs(root, res):
            if not root:
                return res

            print(f"{root.val} - {res} ")

            v1 = dfs(root.left, res+1)
            v2 = dfs(root.right, res+1)

            return max(v1,v2)


        return dfs(root, 0)
        
        