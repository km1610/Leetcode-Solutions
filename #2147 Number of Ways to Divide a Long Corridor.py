class Solution:
    def numberOfWays(self, corridor: str) -> int:
        c = tc = corridor.count('S')
        MOD = (10**9)+7
        if c%2==1 or c==0:
            return 0
        if c==2:
            return 1
        s=0
        i=0
        p=0
        d=1
        while i<len(corridor):
            if corridor[i]=='S':
                if s==2:
                    s=0
                    d=d*(p+1)
                    p=0
                s+=1
                c-=1
            if corridor[i]=='P':
                if c<tc and s==2:
                    p+=1
            i+=1
        return d%MOD
        
