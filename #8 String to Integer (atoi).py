class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:
            return 0

        num = ""

        if s[0] in {'-','+'}:
            num += s[0]
            s = s[1::]

        s = s.lstrip('0')

        for i in s:
            if i.isdigit():
                num = num+i
            else:
                break
        try:
            n = int(num)
            if n< -(2**31):
                n = -(2**31)
            if n>(2**31)-1:
                n = (2**31)-1
            return n
        except:
            return 0
