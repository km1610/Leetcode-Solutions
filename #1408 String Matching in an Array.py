class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substring = []
        n = len(words)

        words.sort(key=len)

        for i in range(n-1):
            for j in range(i+1, n):
                if words[i] in words[j]:
                    substring.append(words[i])
                    break
        
        return substring
