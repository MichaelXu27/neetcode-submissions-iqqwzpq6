class ListNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        prev, nxt = self.tail.prev, self.tail
        prev.next, nxt.prev = new_node, new_node
        new_node.next, new_node.prev = nxt, prev
        self.size += 1

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        prev, nxt = self.head, self.head.next
        prev.next, nxt.prev = new_node, new_node
        new_node.next, new_node.prev = nxt, prev
        self.size += 1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        to_remove = self.tail.prev
        prev, nxt = to_remove.prev, to_remove.next
        prev.next, nxt.prev = nxt, prev
        return to_remove.value


    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        self.size -= 1
        to_remove = self.head.next
        prev, nxt = to_remove.prev, to_remove.next
        prev.next, nxt.prev = nxt, prev
        return to_remove.value
