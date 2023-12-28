class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0

        new_s = ''

        while i<n:
            c = 1
            l = chars[i]
            new_s += l
            while i!=n-1 and chars[i+1]==l:
                c+=1
                i+=1
            if c!=1:
                new_s += str(c)
            i+=1
        
        i = 0

        n = len(new_s)

        for i in range(n):
            chars[i] = new_s[i]

        for i in range(len(chars)-n):
            chars.pop()

        return len(new_s)
