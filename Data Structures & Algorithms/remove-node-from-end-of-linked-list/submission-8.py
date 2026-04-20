# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.n = n

        def f(node):
            if node is None:
                return None
            
            node.next = f(node.next)
            self.n -= 1
            
            if self.n == 0:
                return node.next
            

            return node

        
        return f(head)