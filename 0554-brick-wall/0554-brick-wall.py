class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mp = defaultdict(int)
        for item in wall:
            sums = 0
            for i in range(len(item)-1):
                sums+= item[i]
                mp[sums] += 1
        

        k = 0
        m = 0
        for key,val in mp.items():
            if val > m:
                m = val
                k = key

        return (len(wall) - mp[k]) 
