class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        strings = []
        s = []
        t = maxWidth
        for i in words:
            if not s:
                s.append(i)
                t -= len(i)
            elif len(i)<=t-1:
                s.append(i)
                t -= 1
                t -= len(i)
            else:
                strings.append(s)
                s = [i]
                t = maxWidth - len(i)
        strings.append(s)

        for i in strings:
            print(i)

        ans = []
        for i in range(len(strings)):
            remaining = maxWidth
            for j in strings[i]:
                remaining -= len(j)

            word = strings[i]

            if len(word)>1:
                spaces = remaining//(len(word)-1)
                extra = remaining%(len(word)-1)

            
            if len(word) == 1:
                ans.append(word[0]+" "*remaining)
            elif i==len(strings)-1:
                ans.append(" ".join(word) + " "*(remaining-(len(word)-1)))
            else:
                s = ''
                for j in range(len(word)-1):
                    s += word[j]
                    s += ' '*spaces
                    if extra:
                        s += ' '
                        extra -= 1
                s += word[-1]
                ans.append(s)

        return ans
