class Solution:
    def canCross(self, stones):
        mp = set(stones)
        final = stones[-1]
        dp = {}

        def fun(pos, step):

            if pos == final:
                return True

            if (pos, step) in dp:
                return dp[(pos, step)]

            for jump in [step - 1, step, step + 1]:

                if jump <= 0:
                    continue

                next_pos = pos + jump

                if next_pos in mp:
                    if fun(next_pos, jump):
                        dp[(pos, step)] = True
                        return True

            dp[(pos, step)] = False
            return False

        return fun(0, 0)