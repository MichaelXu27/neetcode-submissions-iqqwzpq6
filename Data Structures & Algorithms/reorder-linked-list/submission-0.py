# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle point
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of list
        node = slow.next
        slow.next = None
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        # splice together
        start = head
        end = prev
        while end:
            temp1 = start.next
            temp2 = end.next
            start.next = end
            end.next = temp1
            start = temp1
            end = temp2
        
            

