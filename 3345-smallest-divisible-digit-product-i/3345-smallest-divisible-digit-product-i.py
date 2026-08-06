class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        prod = 1
        for i in str(n):
            prod = prod*int(i)

        if prod % t ==0:
            return n
        return self.smallestNumber(n+1,t)