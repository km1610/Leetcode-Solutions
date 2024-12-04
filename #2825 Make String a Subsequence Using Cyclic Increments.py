class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i, j = 0, 0
        if len(str2)>len(str1):
            return False

        while j < len(str2):

            while i < len(str1) and str2[j] not in {chr(((((ord(str1[i])-ord('a'))) + 1) % 26) + ord('a')), str1[i]}:
                i += 1
            if i >= len(str1):
                return False
            j += 1
            i += 1

        return True
