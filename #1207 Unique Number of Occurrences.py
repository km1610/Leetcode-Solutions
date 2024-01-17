class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        occur = set()

        for i in freq:
            if freq[i] in occur:
                return False
            occur.add(freq[i)
        return True
