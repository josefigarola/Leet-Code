class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        
        for char in s:
            # check if it's an opening
            if char in brackets:
                stack.append(char)
            else:
                # stack is empty
                if not stack:
                    return False
                # check element from the stack in dic and check
                if brackets[stack.pop()] != char:
                    return False
        
        return not stack