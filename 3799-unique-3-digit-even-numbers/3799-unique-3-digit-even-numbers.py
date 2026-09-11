class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        def fun(subset, used):
            if len(subset) == 3:
                if subset[0] != 0 and subset[2] % 2 == 0:
                    num = subset[0] * 100 + subset[1] * 10 + subset[2]
                    ans.add(num)
                return

            for i in range(len(digits)):
                if i in used:
                    continue

                used.add(i)
                subset.append(digits[i])

                fun(subset, used)

                subset.pop()
                used.remove(i)

        fun([], set())

        return len(ans)