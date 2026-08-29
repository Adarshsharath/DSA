class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = paragraph.lower()

        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace("'", " ")
        paragraph = paragraph.replace(";", " ")

        words = paragraph.split()

        count = {}

        for word in words:
            if word not in banned:
                count[word] = count.get(word, 0) + 1

        maxword = max(count, key=count.get)

        return maxword