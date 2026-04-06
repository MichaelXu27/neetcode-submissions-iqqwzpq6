class ListNode:
    def __init__(self, key, val, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Sentinels
        self.head = ListNode(0, 0)  # LRU sentinel
        self.tail = ListNode(0, 0)  # MRU sentinel
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self._add(node)

            if len(self.cache) > self.capacity:
                # Evict LRU: node right after head
                lru = self.head.nxt
                self._remove(lru)
                del self.cache[lru.key]

    def _remove(self, node: ListNode):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def _add(self, node: ListNode):
        # Insert before tail
        prev = self.tail.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.tail
        self.tail.prev = node