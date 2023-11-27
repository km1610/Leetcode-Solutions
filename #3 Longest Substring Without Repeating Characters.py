class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        max_len = 1
        l = 0
        if len(s)==0:
            return 0
        for i in range(len(s)):
            if s[i] not in char:
                char[s[i]] = i
                max_len = max(max_len,(i-l+1))
            else:
                if char[s[i]]>=l:
                    l = char[s[i]]+1
                    char[s[i]] = i
                else:
                    char[s[i]] = i
                    max_len = max(max_len,(i)-l+1)

        return max_len     
