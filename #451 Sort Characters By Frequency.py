class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        order = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        new_s = ''
        
        for i in order:
            new_s += i[0]*i[1]
        
        return new_s
