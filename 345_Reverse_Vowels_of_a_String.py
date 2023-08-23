class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Set of vowels
        s = list(s) # Manipulation purpose
        
        p1 = 0
        p2 = len(s) - 1 
        
        while(p1 < p2):
            # Check if the letter is in vowels
            if(s[p1] in vowels and s[p2] in vowels):
                s[p1], s[p2] = s[p2], s[p1]  # Swap vowels
                p1 += 1
                p2 -= 1
            elif(s[p1] in vowels):
                p2 -= 1
            else:
                p1 += 1
        
        return "".join(s)