class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxlen = -1
        indices = {}
        for i in range(len(s)):
            if s[i] not in indices:
                indices[s[i]] = i
            else:
                maxlen = max(maxlen,i-indices[s[i]]-1)
        return maxlen
