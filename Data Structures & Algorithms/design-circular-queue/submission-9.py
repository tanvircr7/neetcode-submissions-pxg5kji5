class Node:
    def __init__(self, val):
        self.val, self.prev, self.next = val, None, None

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.k = k
        self.i = 0
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        prev, nxt = self.right.prev, self.right
        node = Node(value)
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        self.q.append(node)
        self.i += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        prev, nxt = self.left, self.left.next.next
        prev.next, nxt.prev = nxt, prev
        self.i -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        if self.left.next == self.right: return True
        return False

    def isFull(self) -> bool:
        if self.i == self.k: return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()