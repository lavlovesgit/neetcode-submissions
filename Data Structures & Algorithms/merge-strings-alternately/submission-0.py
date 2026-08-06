class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        i = 0

        while i < min(len(word1), len(word2)):
            new += word1[i]
            new += word2[i]
            i += 1

        if i < len(word1):
            new += word1[i:]

        if i < len(word2):
            new += word2[i:]

        return new

        
        
            
        