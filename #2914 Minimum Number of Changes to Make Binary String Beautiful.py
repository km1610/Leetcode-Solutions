class Solution:
    def minChanges(self, s: str) -> int:
        curr = s[0]
        changes = 0
        length = 0
        for i in range(len(s)):
            if s[i] == curr:
                length += 1
            else:
                if length%2 == 1:
                    changes += 1
                    length = 0
                else:
                    curr = s[i]
                    length = 1
        return changes
