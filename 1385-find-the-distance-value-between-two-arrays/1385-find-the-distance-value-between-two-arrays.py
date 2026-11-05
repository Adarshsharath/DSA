class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for item in arr1:
            distance = False
            for x in arr2:
                if abs(item-x) <= d:
                    distance = True
                    break
            if not distance:
                count += 1
        return count
