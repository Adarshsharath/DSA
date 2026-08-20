class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        mp = {}

        for row, seat in reservedSeats:
            if row not in mp:
                mp[row] = set()

            mp[row].add(seat)

        count = 2 * n

        for row in mp:
            left = True
            mid = True
            right = True

            for seat in range(2, 6):
                if seat in mp[row]:
                    left = False

            for seat in range(4, 8):
                if seat in mp[row]:
                    mid = False

            for seat in range(6, 10):
                if seat in mp[row]:
                    right = False

            if left and right:
                continue

            elif left or mid or right:
                count -= 1

            else:
                count -= 2

        return count