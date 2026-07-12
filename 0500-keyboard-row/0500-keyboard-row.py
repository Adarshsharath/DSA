class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = ['q','w','e','r','t','y','u','i','o','p']
        second = ['a','s','d','f','g','h','j','k','l']
        third = ['z','x','c','v','b','n','m']

        new = []


        for word in words:
            reject1 = False
            reject2 = False
            reject3 = False
            for i in word:
                if i.lower() not in first:
                    reject1 = True 
            for i in word:
                if i.lower() not in second:
                    reject2 = True
            for i in word:
                if i.lower() not in third:
                    reject3 = True
            
            if not (reject1 and reject2 and reject3):
                new.append(word)
        
        return new
            





