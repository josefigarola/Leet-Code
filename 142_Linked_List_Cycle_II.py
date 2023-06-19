# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Use Floyd's Cycle Detection Algorithm
        slow = head # moves by one
        fast = head # moves by two

        print(slow)
        stack = []
        meeting_point = None  # Track the meeting point

        while(fast.next != None and fast != None):
            if(slow.val not in stack):
                stack.append(slow.val)

            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                tmp = head

                if(slow.val not in stack):
                    stack.append(slow.val)

                while(slow != tmp):
                    slow = slow.next
                    tmp = tmp.next
                
                print(slow.val)
                pos_val = slow.val
                break

        print(stack)

        #return -1
