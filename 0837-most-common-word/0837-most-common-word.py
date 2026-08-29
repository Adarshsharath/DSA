class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace(":", " ")
        paragraph = paragraph.replace("'", " ")
        
        ls = paragraph.split()
        
        banned = [word.lower() for word in banned]
        mp = defaultdict(int)

        for item in ls:
            mp[item] += 1

        maxval = -1
        maxno = ""

        for key, val in mp.items():
            if key not in banned:
                if val > maxval:
                    maxval = val
                    maxno = key

        return maxno
        