class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = {}
        for i in words:
            for j in i:
                if j in freq:
                    freq[j]+=1
                else:
                    freq[j]=1
        n = len(words)
        for i in freq:
            if freq[i]%n!=0:
                return False
        return True
