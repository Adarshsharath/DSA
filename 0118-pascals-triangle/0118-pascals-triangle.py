class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls = []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        ls.append([1])
        ls.append([1,1])

        for i in range(2,numRows):
            prev = ls[i-1]
            new = []
            new.append(prev[0])
            for i in range(1,len(prev)):
                sums = 0
                sums = prev[i]+prev[i-1]
                new.append(sums)
            new.append(prev[len(prev)-1])
            ls.append(new)

        return ls
            

