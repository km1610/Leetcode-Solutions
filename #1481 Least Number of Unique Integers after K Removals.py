class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        keys_freq = sorted(freq,key=lambda x:freq[x])

        for i in keys_freq:
            if k==0:
                break
            if freq[i]<k:
                k-=freq[i]
                freq[i]=0
            else:
                freq[i]-=k
                k=0
        c=0

        for i in freq:
            if freq[i]>0:
                c+=1
        return c
