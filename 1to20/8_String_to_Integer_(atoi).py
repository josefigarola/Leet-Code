class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Read and ignore leading whitespace
        i = 0
        while(i < len(s) and s[i].isspace()):
            i += 1
        
        # Step 2: Check for '+' or '-' sign
        if(i < len(s) and (s[i] == '+' or s[i] == '-')):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1
        
        # Step 3 and Step 4: Read in digits until non-digit character
        num = 0
        while(i < len(s) and s[i].isdigit()):
            digit = int(s[i])
            # Check for integer overflow
            if(num > (INT_MAX - digit) // 10):
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        # Step 5: Apply sign and clamp to 32-bit range
        num *= sign
        return max(INT_MIN, min(INT_MAX, num))