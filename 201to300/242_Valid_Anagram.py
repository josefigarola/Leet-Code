class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Check both lens
        if(len(s) != len(t)):
            return False
        
        # Sort the strings
        if(sorted(s) == sorted(t)):
            return True
