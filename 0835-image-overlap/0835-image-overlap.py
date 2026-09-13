class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ls1 = []
        ls2 = []
        mp = defaultdict(int)
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    ls1.append((i,j))
                if img2[i][j] == 1:
                    ls2.append((i,j))

        for i in ls1:
            for j in ls2:
                X = i[0] - j[0]
                Y = i[1] - j[1]
                mp[(X,Y)] += 1

        return max(mp.values(),default=0)