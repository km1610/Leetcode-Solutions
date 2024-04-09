class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        t=0
        n=len(tickets)
        while tickets[k] != 0:
            if tickets[i]>0:
                tickets[i]-=1
                t+=1
            i = (i+1)%n
        return t
