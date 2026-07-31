# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.n = n

        def f(node):
            if not node:
                return None
            
            node.next = f(node.next)
            self.n -= 1

            print(f"{node.val}")
            if self.n == 0:
                print(f"N = 0")
                return node.next 
            print(f"N ok")
            return node


        
        return f(head)