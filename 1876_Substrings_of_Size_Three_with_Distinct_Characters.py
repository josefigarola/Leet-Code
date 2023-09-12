class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if(len(s) < 3):
            return 0

        counter = 0

        for i in range(2,len(s)):
            current = s[i-2:i+1]
            if(current[0] != current[1] and current[1] != current[2] and current[0] != current[2]):
                counter += 1

        return counter