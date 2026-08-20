class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board[0])
        col = len(board)

        def f(i,j,k):
            if k == len(word):
                return True

            if (i >= col or i < 0) or (j<0 or j>= row):
                return False


            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = (f(i-1,j,k+1) or f(i,j+1,k+1) or f(i+1,j,k+1) or f(i,j-1,k+1))

            board[i][j] = temp 
            return found

        for i in range(col):
            for j in range(row):
                if (f(i,j,0)):
                    return True
        return False



