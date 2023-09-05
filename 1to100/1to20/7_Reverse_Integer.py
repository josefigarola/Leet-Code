class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if(x == 0):
            return 0
        
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        
        while(x > 0):
            digit = x % 10
            # Check for integer overflow before appending a digit
            if(reversed_num > (INT_MAX - digit) // 10):
                return 0
            reversed_num = reversed_num * 10 + digit
            x //= 10
        
        return sign * reversed_num