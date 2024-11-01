class Solution:
    def makeFancyString(self, s: str) -> str:
        string = ""
        l = 0
        curr = ""
        pointer = ""
        for i in s:
            if i==curr:
                l+=1
            else:
                curr = i
                l = 1

            if l>2:
                continue
            else:
                string += i
        return string
