class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ls = []

        if rowIndex==0:
            return [1]

        if rowIndex == 1:
            return [1,1]

        def generate(numRows: int) -> List[List[int]]:
            
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

        generate(rowIndex+1)

        return ls[-1]

        
            