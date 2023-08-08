class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 are not palindromes
        if(x < 0 or (x % 10 == 0 and x != 0)):
            return False
        
        reversed_num = 0
        original_x = x
        
        while(x > 0):
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return original_x == reversed_num