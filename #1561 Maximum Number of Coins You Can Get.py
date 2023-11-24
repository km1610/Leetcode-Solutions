class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l = 0
        h = len(piles)-1
        piles.sort()
        p=0
        while l<=h:
            print(h,h-1,l)
            pile = [piles[h],piles[h-1],piles[l]]
            p+=pile[1]
            l+=1
            h-=2
        return p
        
