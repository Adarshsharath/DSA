class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append((i,j))
        # print(zeroes)
        while zeroes:
            (x,y) = zeroes.pop()
            #vertical - j = y and i from 0 to n-1 
            for i in range(len(matrix)):
                if matrix[i][y]!=0:
                    matrix[i][y] = 0
            for j in range(len(matrix[0])):
                if matrix[x][j] != 0:
                    matrix[x][j] = 0