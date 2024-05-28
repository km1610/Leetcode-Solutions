class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curr_cost = 0
        length = 0
        max_length = -float('inf')

        n = len(s)
        j = 0

        for i in range(n):
            curr_cost += abs(ord(s[i])-ord(t[i]))
            if curr_cost<=maxCost:
                length+=1
            else:
                curr_cost -= abs(ord(s[j])-ord(t[j]))
                j+=1

        return length
