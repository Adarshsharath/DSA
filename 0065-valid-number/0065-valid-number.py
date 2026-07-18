class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exp = False

        for i, ch in enumerate(s):

            if ch.isdigit():
                seen_digit = True

            elif ch == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in "eE":
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False

            elif ch in "+-":
                if i != 0 and s[i - 1].lower() != 'e':
                    return False

            else:
                return False

        return seen_digit