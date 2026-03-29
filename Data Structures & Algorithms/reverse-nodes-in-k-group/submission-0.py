class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        i = 1
        while node and i < k:
            node = node.next
            i += 1
        if not node:
            return head
        ret = node
        
        last_tail = None
        node = head
        while node:
            lookahead = node
            for _ in range(k):
                if not lookahead: break
                lookahead = lookahead.next
            else:
                prev = lookahead
                curNode = node
                for _ in range(k):
                    temp = curNode.next
                    curNode.next = prev
                    prev = curNode
                    curNode = temp
                if last_tail:
                    last_tail.next = prev
                last_tail = node
                node = lookahead
                continue
            break
        return ret