# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.n = n
        
        def rec(node):
            if not node:
                return None
            node.next = rec(node.next)
            self.n -= 1          # Modifies instance variable
            if self.n == 0:
                return node.next
            return node
        
        return rec(head)

        