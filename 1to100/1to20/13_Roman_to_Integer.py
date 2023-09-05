class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }

        out = 0
        #s = 'MCMXCIV'
        p1 = 0

        while(p1 < len(s)):
            # check special cases for char and next char
            if(p1 < len(s) - 1 and s[p1:p1+2] in roman):
                out += roman[s[p1:p1+2]]
                p1 += 2
            else:
                out += roman[s[p1]]
                p1 += 1

        print(out)

        return out