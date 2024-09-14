class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = ["" for i in range(len(words))]
        for i in range(len(words)):
            sets[i] = set(words[i])
        mlp = 0
        for i in range(len(sets)-1):
            for j in range(i+1,len(sets)):
                if len(sets[i].union(sets[j]))==len(sets[i])+len(sets[j]):
                    mlp = max(mlp,len(words[i])*len(words[j]))
        return mlp
