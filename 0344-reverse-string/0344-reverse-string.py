class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def fun(l,r):
            if l >= r:
                return
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            fun(l+1,r-1)

        fun(0,len(s)-1)
        