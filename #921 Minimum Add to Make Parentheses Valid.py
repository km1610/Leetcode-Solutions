class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        x = y = 0
        for i in s:
            if i == '(':
                x += 1
            elif i == ')' and x>0:
                x -= 1
            else:
                y += 1
        return x + y
