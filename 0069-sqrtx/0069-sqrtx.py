class Solution:
    def mySqrt(self, x: int) -> int:
        def re(num,x):
            if num*num>x:
                return num-1
            return re(num+1,x)

        return re(1,x)


            
        