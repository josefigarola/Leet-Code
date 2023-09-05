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
        stack = []

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
                break

        print('stack', stack)
        
        for i in range(len(stack)-1):
            if(stack[i] == slow.val):
                msg = 'tail connects to node index ' + str(i)
                print(msg)
                return msg

        #return -1
