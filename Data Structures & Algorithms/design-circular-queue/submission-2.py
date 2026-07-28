class Node:
    def __init__(self, value):
        self.val = value
        self.prev = self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.q = []
        self.k = k
        self.left, self.right = Node(0), Node(0)
        self.left.next, self.right.prev = self.right, self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        node = Node(value)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt
        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        prev, nxt = self.left, self.left.next.next
        tmpval = prev.next.val
        prev.next = nxt
        nxt.prev = prev
        self.q.remove(tmpval)
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False

    def isFull(self) -> bool:
        return len(self.q)==self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()