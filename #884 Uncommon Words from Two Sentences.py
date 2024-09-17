from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        s1 = s1.split()
        s2 = s2.split()
        freq = defaultdict(int)

        for i in s1:
            freq[i] += 1
        for i in s2:
            freq[i] += 1
        
        for i in freq:
            if freq[i] == 1:
                res.append(i)

        return res
