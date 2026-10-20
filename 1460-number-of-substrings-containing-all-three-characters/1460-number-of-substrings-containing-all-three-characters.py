class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        a_ls = [-1] * n
        b_ls = [-1] * n
        c_ls = [-1] * n


        i = 0
        for ch in s:
            if ch == "a":
                k = i
                while k >= 0 and a_ls[k] == -1:
                    a_ls[k] = i
                    k -= 1
            i += 1

        i = 0
        for ch in s:
            if ch == "b":
                k = i
                while k >= 0 and b_ls[k] == -1:
                    b_ls[k] = i
                    k -= 1
            i += 1

        i = 0
        for ch in s:
            if ch == "c":
                k = i
                while k >= 0 and c_ls[k] == -1:
                    c_ls[k] = i
                    k -= 1
            i += 1


        count = 0

        for i in range(n):
            if a_ls[i] != -1 and b_ls[i] != -1 and c_ls[i] != -1:
                first = max(a_ls[i], b_ls[i], c_ls[i])
                count += n - first

        return count