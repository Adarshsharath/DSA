class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums = 0
        prod = 1
        for i in str(n):
            sums += int(i)
            prod *= int(i)

        num = sums+prod

        if not n%num:
            return True
        return False