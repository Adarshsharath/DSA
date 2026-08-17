class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = defaultdict(list)

        row = 0
        direction = 1

        for ch in s:

            rows[row].append(ch)

            if row == 0:
                direction = 1

            elif row == numRows - 1:
                direction = -1

            row += direction

        ans = ""

        for i in range(numRows):
            ans += "".join(rows[i])

        return ans