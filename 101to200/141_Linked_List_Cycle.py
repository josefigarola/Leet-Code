# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Use Floyd's Cycle Detection Algorithm
        if(not head or not head.next):
            return False

        slow = head # moving by one
        fast = head.next # moving by two

        while(slow != fast):
            # when fast reaches the end, there's no cycle
            if(not fast or not fast.next):
                return False
            # move the pointers
            slow = slow.next
            fast = fast.next.next

        return True