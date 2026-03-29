# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        dq = deque()
        dq.append(root)

        while dq:
            node = dq.popleft()

            if node is None:
                continue
            
            node.left, node.right = node.right, node.left

            dq.append(node.left)
            dq.append(node.right)

        
        return root
