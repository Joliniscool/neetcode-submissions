class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #for len smaller then add rest 
        
        #if word1 > word 2 then x = word1 else = word2
        x = word1 if (len(word1) < len(word2)) else word2
        y = word1 if len(word1) > len(word2) else word2
        final = []
        for i in range(len(x)):
            final.append(word1[i])
            final.append(word2[i])
        final.append(y[len(x):])
        return "".join(final)

        #[:] word of 
            
