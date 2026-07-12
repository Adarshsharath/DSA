class Solution:
    def bintoin(self,x):
        ans = 0
        for bit in x:
            ans = ans*2+int(bit)
        return ans
    def addBinary(self, a: str, b: str) -> str:
        num1 = self.bintoin(a)
        num2 = self.bintoin(b)

        sum = num1 + num2

        return bin(sum)[2::]

