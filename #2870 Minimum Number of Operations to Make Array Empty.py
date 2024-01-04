class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0

        freq = {}

        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        def getop(n,i):
            o = 0
            for _ in range(i):
                n-=2
                o+=1
            
            while n>0:
                n-=3
                o+=1
            print(o)
            return o

        for i in freq:
            if freq[i]==1:
                return -1
            elif freq[i]==2:
                op+=1
            elif freq[i]%3==0:
                op+=getop(freq[i],0)
            elif freq[i]%3==1:
                op+=getop(freq[i],2)
            elif freq[i]%3==2:
                op+=getop(freq[i],1)
        return op
