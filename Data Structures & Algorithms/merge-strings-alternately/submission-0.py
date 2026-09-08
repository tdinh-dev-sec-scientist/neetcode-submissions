class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        s = 0

        while s < len(word1) or s < len(word2):
            if s < len(word1):
                res.append(word1[s])
            if s < len(word2):
                res.append(word2[s])
                
            s+= 1
        return "".join(res)