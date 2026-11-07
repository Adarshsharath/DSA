class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        ls = []

        while top <= bottom and left <= right:

            for j in range(left, right + 1):
                ls.append(matrix[top][j])
            top += 1

            for i in range(top, bottom + 1):
                ls.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ls.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ls.append(matrix[i][left])
                left += 1

        return ls