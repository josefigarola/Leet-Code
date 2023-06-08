class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        char_dict = {}
        longest_len = 0
        left = 0
        
        for right in range(n):
            if s[right] in char_dict and char_dict[s[right]] >= left:
                left = char_dict[s[right]] + 1
            char_dict[s[right]] = right
            longest_len = max(longest_len, right - left + 1)
        
        return longest_len
