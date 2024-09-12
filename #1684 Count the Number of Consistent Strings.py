class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        consistent = 0

        for i in words:
            c = 1
            for j in i:
                if j not in allowed:
                    c = 0
            consistent += c
        return consistent
