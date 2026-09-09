class Solution:
    def countCommas(self, n: int) -> int:
        if n < 999:
            return 0
        x = len(str(n))
        s = "999"
        k="999"
        def fun(n,s):
            print(s)
            if n - int(s)>0:
                return n - int(s) + fun(n,s+k)
            return 0
        return fun(n,s)
        
        