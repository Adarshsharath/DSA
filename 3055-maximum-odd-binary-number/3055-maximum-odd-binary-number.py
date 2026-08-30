class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ls1 = []
        ls0 = []
        for i in s:
            if i == "1":
                ls1.append(i)
            if i == "0":
                ls0.append(i)


        new = []
        if len(ls1)>1:
            for i in range(len(ls1)-1):
                new.append(ls1[i])
        if ls0:
            for i in range(len(ls0)):
                new.append(ls0[i])

        new.append(ls1[-1])

        return "".join(new)
            