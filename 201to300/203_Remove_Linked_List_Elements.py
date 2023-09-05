# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        current = dummy

        while(current.next):
            # If val is found
            if(current.next.val == val):
                # Skip this value
                current.next = current.next.next
            else:
                # Move current to the next node
                current = current.next

        return dummy.next