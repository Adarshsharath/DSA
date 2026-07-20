class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        stack = []

        rows = len(grid)
        cols = len(grid[0])

        for row in grid:
            for num in row:
                stack.append(num)

        while k:
            k -= 1

            last = stack[-1]

            for i in range(len(stack) - 1, 0, -1):
                stack[i] = stack[i - 1]

            stack[0] = last

        grid = []
        idx = 0

        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(stack[idx])
                idx += 1
            grid.append(temp)

        return grid