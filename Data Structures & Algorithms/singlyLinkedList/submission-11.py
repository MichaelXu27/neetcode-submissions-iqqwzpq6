class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(0)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        i = 0
        dummy = self.head.next
        while dummy:
            if i == index:
                break
            dummy = dummy.next
            i += 1
        return dummy.value if dummy else -1

    def insertHead(self, val: int) -> None:
        dummy = self.head.next
        if not dummy:
            temp = ListNode(val)
            self.head.next = temp
            self.tail = self.head.next
        else:            
            temp = ListNode(val)
            self.head.next = temp
            temp.next = dummy

    def insertTail(self, val: int) -> None:
        temp = ListNode(val)
        self.tail.next = temp
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        dummy = self.head.next
        prev = None
        while dummy:
            if i == index:
                if prev == None:
                    self.head.next = dummy.next
                    if self.head.next == None:
                        self.tail = self.head
                else:
                    prev.next = dummy.next
                    if prev.next == None:
                        self.tail = prev
                
                return True
            i += 1
            prev = dummy
            dummy = dummy.next
        return False

    def getValues(self) -> List[int]:
        valList = []
        dummy = self.head.next
        while dummy:
            valList.append(dummy.value)
            dummy = dummy.next
        return valList