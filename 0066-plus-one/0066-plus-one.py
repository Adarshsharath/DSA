class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        i = len(digits) - 1

        num = digits[i] + 1
        carry = num // 10
        digits[i] = num % 10

        if carry == 0:
            return digits

        i -= 1

        while i >= 0 and carry:
            num = digits[i] + carry
            carry = num // 10
            digits[i] = num % 10
            i -= 1

        if carry:
            digits.insert(0, 1)

        return digits

#Alternate
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:

#         i = len(digits) - 1

#         while i >= 0:
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits

#             digits[i] = 0
#             i -= 1

#         return [1] + digits
