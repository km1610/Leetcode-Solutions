class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}

        for i in trust:
            a,b = i[0],i[1]
            if a in trusts:
                trusts[a].add(b)
            else:
                trusts[a] = {b}
        
        k = 0
        judge = -1
        for i in range(1,n+1):
            if i not in trusts:
                k+=1
                judge = i
        
        if k!=1 :
            return -1
        
        p = 0

        for i in trusts:
            if judge in trusts[i]:
                p+=1
        
        if p==n-1:
            return judge
        return -1
