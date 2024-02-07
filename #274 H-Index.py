class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i = 0
        j = 1
        while j<=len(citations):
            if citations[-j]>=i+1:
                i+=1
            j+=1
        return i
