class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        resLen = 0

        for i in range(len(s)):
            p1, p2 = i, i
            # Odd len
            # while it is a palindrome
            while(p1>=0 and p2 <len(s) and s[p1] == s[p2]):
                if((p2-p1+1)> resLen): # if it is the longest palindrome found
                    #print('palindrome found')
                    res = s[p1:p2+1]
                    #print(res)
                    resLen = p2-p1+1
                p1 -= 1
                p2 += 1

            # Even len
            p1,p2 = i,i+1
            while(p1>=0 and p2 <len(s) and s[p1] == s[p2]):
                if((p2-p1+1)> resLen):
                    res = s[p1:p2+1]
                    resLen = p2-p1+1
                p1 -= 1
                p2 += 1

        return res