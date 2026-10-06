class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        old = [row[:] for row in board]

        def result(i,j):
            sums = 0
            l = 0
            r = 0
            t = 0
            d = 0
            tl = 0
            tr = 0
            dl = 0
            dr = 0

            if j > 0:#left
                if old[i][j-1]:
                    l = 1
            if j<len(old[0])-1:#right
                if old[i][j+1]:
                    r = 1
            if i >0:#top
                if old[i-1][j]:
                    t = 1
            if i < len(old)-1:#down
                if old[i+1][j]:
                    d = 1
            if j > 0 and i > 0:#top-left
                if old[i-1][j-1]:
                    tl = 1
            if j<len(old[0])-1 and i>0:#top-right
                if old[i-1][j+1]:
                    tr = 1
            if j > 0 and i < len(old)-1:#bottom-left
                if old[i+1][j-1]:
                    dl = 1
            if j < len(old[0])-1 and i < len(old)-1:#bottom-right
                if old[i+1][j+1]:
                    dr = 1

            sums = l+r+t+d+tl+tr+dl+dr

            return sums




        for i in range(len(board)):
            for j in range(len(board[0])):
                x = result(i,j)
                print((i,j),"->",x)
                
                if board[i][j] == 1:
                    if x < 2 or x > 3:
                        board[i][j] = 0
                else:
                    if x == 3:
                        board[i][j] = 1
        
