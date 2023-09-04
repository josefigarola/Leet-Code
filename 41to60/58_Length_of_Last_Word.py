class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        p1 = 0

        while(p1 < len(s)):
            print(s[p1],length)
            # if the p1 is not a space
            if(s[p1] != ' '):
                length += 1
            # ignore everything by reseting the length if theres more to the string
            elif(p1+1 < len(s) and s[p1+1] != ' '):
                length = 0

            p1+= 1 

        return length
