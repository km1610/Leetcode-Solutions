class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for i in word:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        freq_keys = sorted(freq, key=lambda x: freq[x], reverse=True)
        keys = 8
        effort = 1
        cost = 0

        for i in freq_keys:
            if keys==0:
                keys=8
                effort+=1
            keys-=1
            cost+=effort*freq[i]
        return cost
