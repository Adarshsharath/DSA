class Solution:
    def reverse(self, x: int) -> int:
        negative = False

        if x < 0:
            negative = True
            x = abs(x)

        rev = int(str(x)[::-1])

        if negative:
            rev = -rev

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev