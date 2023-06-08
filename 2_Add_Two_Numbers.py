# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # current values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            digit_sum = val1 + val2 + carry
            #print(digit_sum)
            carry = digit_sum // 10  # Calculate the new carry
            #print(carry)
            digit = digit_sum % 10  # Calculate the digit value
            #print(digit)
            
            # Create a new node with the digit value and connect it to the result list
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the input lists, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
    
        return dummy.next 