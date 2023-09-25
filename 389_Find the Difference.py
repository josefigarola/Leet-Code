class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0

        # XOR through every char
        #print(f'first loop, result: {result}')
        for char in s:
            result ^= ord(char) # get ASCII
            #print(f"XOR with '{char}' - Result: {result}")

        #print(f'second loop, result: {result}')
        for char in t:
            result ^= ord(char)
            #print(f"XOR with '{char}' - Result: {result}")

        #print(result)
        return chr(result)

        