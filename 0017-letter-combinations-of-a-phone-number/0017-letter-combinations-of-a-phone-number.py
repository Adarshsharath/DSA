class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mp = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 0:
            return []

        ls = []

        def fun(pos, substr):

            if pos == len(digits):
                ls.append(substr)
                return

            for ch in mp[digits[pos]]:
                fun(pos + 1, substr + ch)

        fun(0, "")

        return ls