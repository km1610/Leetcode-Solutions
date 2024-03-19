class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m,n = len(s),len(t)

        if m!=n:
            return False

        freq_s = {}
        freq_t = {}

        for i in range(n):
            if s[i] in freq_s:
                freq_s[s[i]]+=str(i)
            else:
                freq_s[s[i]]=str(i)
            
            if t[i] in freq_t:
                freq_t[t[i]]+=str(i)
            else:
                freq_t[t[i]]=str(i)

        for i in range(m):
            if freq_s[s[i]]!=freq_t[t[i]]:
                return False
        return True
