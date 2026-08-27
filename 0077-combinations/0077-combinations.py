class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        n = [i for i in range(1,n+2)]
        ls = []

        def fun(idx,subset,count):
            if idx == len(n):
                return
            if count == k:
                ls.append(subset[:])
                return

            subset.append(n[idx])
            count+=1
            fun(idx+1,subset,count)

            subset.pop()
            count-=1

            fun(idx+1,subset,count)
        fun(0,[],0)

        return ls