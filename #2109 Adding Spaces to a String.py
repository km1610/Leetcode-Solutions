class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        spaces = set(spaces)
        new_s = ""
        i = len(s)-1

        while i>=0:
            if i+1 in spaces:
                new_s = " " + new_s

            new_s = s[i] + new_s
            i -= 1

        if 0 in spaces:
            new_s = " " + new_s

        return new_s
