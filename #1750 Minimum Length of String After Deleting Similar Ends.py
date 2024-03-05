class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)

        prefix, suffix = 0, n-1

        while prefix<suffix:
            if s[prefix]==s[suffix]:
                char = s[prefix]
                while s[prefix]==char and prefix<suffix:
                    prefix+=1
                while s[suffix]==char and prefix<=suffix:
                    suffix-=1
            else:
                return suffix-prefix+1

        return suffix-prefix+1
