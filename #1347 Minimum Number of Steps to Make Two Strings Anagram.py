class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            if s[i] in freq_s:
                freq_s[s[i]] += 1
            else:
                freq_s[s[i]] = 1

            freq_t[s[i]] = 0
            
        for i in range(len(t)):

            if t[i] in freq_t:
                freq_t[t[i]] += 1

        steps = 0

        for i in freq_s:
            diff = freq_s[i]-freq_t[i]
            if diff>=0:
                steps+=diff

        return steps
