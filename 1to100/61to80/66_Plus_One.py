class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1

        for i in range(n - 1, -1, -1):
            total = digits[i] + carry

            if total >= 10:
                carry = 1
                digits[i] = total % 10
            else:
                carry = 0
                digits[i] = total

        if carry:
            digits.insert(0, carry)

        return digits